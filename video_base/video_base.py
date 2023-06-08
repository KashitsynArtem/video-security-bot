import cv2
from io import BytesIO
import os


async def get_screenshot():
    cap = cv2.VideoCapture(os.environ.get('RTSP'))
    _, frame = cap.read()

    is_success, im_buf_arr = cv2.imencode('.png', frame)
    io_buf = BytesIO(im_buf_arr)
    io_buf.seek(0)

    return io_buf



