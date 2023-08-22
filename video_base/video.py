import asyncio
from io import BytesIO

import cv2

from settings import Settings
from telegram_bot.bot import send_alert, send_error
from utils.stats import stats
from utils.time_base import get_current_time, delta_time


class VideoProcessService:
    def __init__(self,
                 src):
        self.src = src
        self.frame = None
        self.previous_frame = None
        self.motion_detection_mode = True
        self.motion_detected = False
        self.last_time_alert = 0
        self.current_time = 0

    async def video_capture(self):
        video_capture = cv2.VideoCapture(self.src)
        cv2.VideoCapture()
        return video_capture

    async def detect_motion(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if self.previous_frame is None:
            self.previous_frame = gray

        frame_delta = cv2.absdiff(self.previous_frame, gray)
        thresh = cv2.threshold(frame_delta, 30, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 500:
                self.motion_detected = True
                break

        self.previous_frame = gray

    async def alert_motion_detection(self):
        if self.motion_detected is True:

            if await delta_time(self.current_time, self.last_time_alert) > 10:

                screen = await self.screenshot()
                await asyncio.sleep(0)
                await send_alert(screen)
                self.last_time_alert = await get_current_time()

            self.current_time = await get_current_time()
            self.motion_detected = False

    async def screenshot(self):
        is_success, im_buf_arr = cv2.imencode('.png', self.frame)
        io_buf = BytesIO(im_buf_arr)
        io_buf.seek(0)

        return io_buf

    async def preprocess_frame(self, video_capture):
        ret, frame = video_capture.read()

        if ret is None:
            await send_error('Cam offline')
            await asyncio.sleep(10)

        frame = cv2.resize(frame, (640, 480))
        self.frame = frame

    async def read_video(self):
        video_capture = await self.video_capture()
        self.current_time = await get_current_time()
        self.last_time_alert = await get_current_time()

        while True:
            try:
                await self.preprocess_frame(video_capture)

                if self.motion_detection_mode is True:
                    await self.detect_motion(self.frame)
                    await self.alert_motion_detection()

                cv2.imshow('Video Stream', self.frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                await asyncio.sleep(0)

                await stats()

            except Exception as ex:
                print(f'{ex}')
                continue

        video_capture = await self.video_capture()
        video_capture.release()
        cv2.destroyAllWindows()

    async def switch_motion_detection_mode(self):
        self.motion_detection_mode = not self.motion_detection_mode

    async def get_motion_detection_mode(self):
        return self.motion_detection_mode


VideoProcess = VideoProcessService(Settings.RTSP)


