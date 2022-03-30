import numpy as np
import cv2
import imutils
#import pi_camera
#import matplotlib as plt
#=======
#import camera
#from camera import Camera

try:
 from .camera import Camera  # For running app
except ImportError:
 from camera import Camera  # For running main

#from .pi_camera import Camera # For Raspberry Pi

font = cv2.FONT_HERSHEY_COMPLEX

class OpenCVController(object):

    def __init__(self):
        self.current_color = [False, False, False]
        self.camera = Camera()
        print('OpenCV controller initiated')

    #@property
    def process_frame(self):
        frame = self.camera.get_frame()
        # ...
        print('Monitoring')
        #cv2.imshow('Frame', frame)
        #cv2.imwrite('/home/lokesh/Desktop/wise2021groupe/task1_opencv_control/test_frames', frame)

        jpg_as_np = np.fromstring(frame, np.uint8)
        frame = cv2.imdecode(jpg_as_np, cv2.COLOR_BGR2RGB)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # red color
        lower_red = np.array([0, 53, 90])  # approx lower red: [0, 100, 90]
        upper_red = np.array([3, 255, 156])  # approx upper red: [179, 255, 156]
        mask_red = cv2.inRange(hsv, lower_red, upper_red)

        # red color 2nd mask
        lower_red1 = np.array([170, 100, 100])
        upper_red1 = np.array([179, 255, 255])
        mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)

        maskr = mask_red + mask_red1

        # yellow color
        lower_yellow = np.array([22, 50, 80])  # approx lower yellow: [21, 125, 105]
        upper_yellow = np.array([32, 255, 255])  # approx upper yellow: [33, 255, 255]
        mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # purple color
        lower_purple = np.array([120, 0, 0])  # approx lower purple: [130, 125, 105]
        upper_purple = np.array([159, 255, 255])  # approx upper purple: [147, 255, 255]
        mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)

        # green color
        lower_green = np.array([40, 55, 80])  # approx lower green: [38, 125, 105]
        upper_green = np.array([90, 255, 255])  # approx upper green: [83, 255, 255]
        mask_green = cv2.inRange(hsv, lower_green, upper_green)

        com_mask = mask_yellow + mask_purple + mask_green
        # Contours Detection
        con1 = cv2.findContours(com_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        con1 = imutils.grab_contours(con1)

        con2 = cv2.findContours(maskr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        con2 = imutils.grab_contours(con2)

        con3 = cv2.findContours(mask_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        con3 = imutils.grab_contours(con3)

        con4 = cv2.findContours(mask_purple, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        con4 = imutils.grab_contours(con4)

        con5 = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        con5 = imutils.grab_contours(con5)

        # loop for contouring
        for c in con2:

            arear = cv2.contourArea(c)
            if arear > 2000:
                #frame = cv2.drawContours(frame, [c], -1, (0, 0, 255), 3)
                xr, yr, wr, hr = cv2.boundingRect(c)
                xr1 = xr + wr
                yr1 = yr + hr
                frame = cv2.rectangle(frame, (xr, yr), (xr1, yr1), (0, 0, 255), 3)
                cv2.putText(frame, "Red_Marker", (xr,yr), font, 0.5, (0, 0, 255))

        for c in con3:

            areay = cv2.contourArea(c)

            if areay > 6000:
                #frame = cv2.drawContours(frame, [c], -1, (0, 0, 255), 3)
                xy, yy, wy, hy = cv2.boundingRect(c)
                xy1 = xy + wy
                yy1 = yy + hy
                frame = cv2.rectangle(frame, (xy, yy), (xy1, yy1), (255, 255, 0), 3)
                cv2.putText(frame, "Yellow_Region", (xy,yy), font, 0.5, (255, 255, 0))

        for c in con4:

            areap = cv2.contourArea(c)

            if areap > 5000:
                #frame = cv2.drawContours(frame, [c], -1, (0, 0, 255), 3)
                xp, yp, wp, hp = cv2.boundingRect(c)
                xp1 = xp + wp
                yp1 = yp + hp
                frame = cv2.rectangle(frame, (xp, yp), (xp1, yp1), (128, 0, 128), 3)
                cv2.putText(frame, "Purple_Region", (xp,yp), font, 0.5, (128, 0, 128))

        for c in con5:

            areag = cv2.contourArea(c)

            if areag > 5000:
                #frame = cv2.drawContours(frame, [c], -1, (0, 0, 255), 3)
                xg, yg, wg, hg = cv2.boundingRect(c)
                xg1 = xg + wg
                yg1 = yg + hg
                frame = cv2.rectangle(frame, (xg, yg), (xg1, yg1), (0, 255, 0), 3)
                cv2.putText(frame, "Green_Region", (xg,yg), font, 0.5, (0, 128, 0))

        if xp < xr1 and xr < xg1:
            self.current_color = [True, True, False]
            print("green and purple")
        elif xr1 > xy and xr < xp1:
            print("yelllow and purple")
            self.current_color = [False, True, True]

        elif xr1 > xp and xr < xp1:
            print("purple")
            self.current_color = [False, True, False]
        elif xr1 > xy and xr < xy1:
            print("yellow")
            self.current_color = [False, False, True]
        elif xr1 > xg and xr < xg1:
            print("green")
            self.current_color = [True, False, False]
        else:
            print("0ut of zone")
            self.current_color = [False, False, False]

        return cv2.imencode(".jpg", frame)[1].tobytes()

    def get_current_color(self):
        return self.current_color
