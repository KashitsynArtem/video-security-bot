Implemented in Python using the OpenCV module.<p>
  <p align="center">
    <a href="https://github.com/opencv/opencv">
      <img src="https://img.shields.io/badge/built%20with-OpenCV-green.svg" />
    </a>
    <a href="https://github.com/aiogram/aiogram">
    	<img src="https://img.shields.io/badge/built%20with-aiogram2-blue.svg" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>
  </p>

## This is a simple version of a security bot.

A more complex version with a db is planned, with the ability to connect multiple cameras, as well as with limited access to different users. [Link](https://github.com/KashitsynArtem/).

## Problem / Motivation:
in many video surveillance systems (Hikvision Digital Technology, Dahua Technology and others) there are no notifications on smartphones. Often, if some event occurs (e.g. movement in the frame), then several options are available: sound signal (physically on the camera or DVR), sending email, alarm output.
Also, you can't control the detection mode quickly. For example, if you are at home and the movement in the frame is constant, then notifications will come one after another.

## Solution:
This application processes the RTSP stream of the video camera. In cases where there is movement in the frame - sends a screenshot to the telegram bot. You can also quickly switch the detection mode.

## Bot commands:
**/sc** - *sends a screenshot from the camera to the bot.*
**/on_detection_mode** - *enables detection mode.*
**/off_detection_mode** - *disables detection mode.*
**/stats** - *sends data: CPU load and memory used.*
