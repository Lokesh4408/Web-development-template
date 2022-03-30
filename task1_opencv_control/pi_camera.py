import os

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


class Camera(object):
    def __init__(self):
        #directory = os.path.join(os.path.dirname(__file__), 'test_frames')
        # self.test_frames_name = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
        # self.frames = [open(os.path.join(directory, f), 'rb').read() for f in self.test_frames_name
        self.video = cv2.VideoCapture(0)
        '''camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera, size=(640, 480))
        time.sleep(0.1)

        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            #cv2.imshow("Frame", image)
            #key = cv2.waitKey(1) & 0xFF
            rawCapture.truncate(0)

            #if key == ord("q"):
                #break'''

    def get_frame(self):
        #random_index = int(time()) % 4
        #print('Frame', self.test_frames_name[random_index])

        ret, frames = self.video.read()
        return frames
