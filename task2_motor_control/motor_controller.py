try:
    from .fake_gpio import GPIO # For running app
except ImportError:
    from fake_gpio import GPIO # For running main
    
#import RPi.GPIO as GPIO # For testing in Raspberry Pi

import time
from time import sleep 
import sys
import random
class MotorController(object):

  def __init__(self):
    self.working = False
    self.running = False

  def start_motor(self):
        self.running = True
        self.working = True
        self.PIN_STEP = 25 # do not change
        self.PIN_DIR = 8 # do not change
        CW = random.choice((0,1))
        #Declaring variables
        SPR = 400 #steps per revolution. i.e 90/0.225 degrees per step (random rotation)
        SPR_1 = 1200 #steps per revolution. i.e 270/0.225 degrees per step (random rotation)
        #CW = 0  # Clockwise Rotation
        #CCW = 1  # Counterclockwise Rotation
        delay = 0.0200
        
        while(self.running == True and CW==0):
            self.working = True
            print('Motor started')

            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.PIN_STEP, GPIO.OUT)
            GPIO.setup(self.PIN_DIR, GPIO.OUT)
            GPIO.output(self.PIN_DIR, CW)
            
            #GPIO.output(self.PIN_DIR, CCW)
            step_count = random.choice((SPR, SPR_1))
            for x in range(step_count):
              GPIO.output(self.PIN_STEP, GPIO.HIGH)
              time.sleep(delay)
              GPIO.output(self.PIN_STEP, GPIO.LOW)
              time.sleep(delay)
              if step_count ==SPR:
                    print('Rotating 90◦ degrees in clockwise direction')
              else: 
                    print('Rotating 270◦ degrees in clockwise direction')
        #self.working = False

        while(self.running == True and CW==1):
              #time.sleep(2)
              GPIO.setmode(GPIO.BCM)
              GPIO.setup(self.PIN_STEP, GPIO.OUT)
              GPIO.setup(self.PIN_DIR, GPIO.OUT)
              GPIO.output(self.PIN_DIR, CW)
              
              step_count = random.choice((SPR, SPR_1))
              for x in range(step_count):
                GPIO.output(self.PIN_STEP, GPIO.HIGH)
                time.sleep(delay)
                GPIO.output(self.PIN_STEP, GPIO.LOW)
                time.sleep(delay)
                if step_count ==SPR:
                      print('Rotating 90◦ degrees in anticlockwise direction')
                else:
                      print('Rotating 270◦ degrees in anticlockwise direction')
                    
        time.sleep(2)
        self.working = False
        
        if self.running == True and self.working == False and CW==0:
              GPIO.setmode(GPIO.BCM)
              GPIO.setup(self.PIN_STEP, GPIO.OUT)
              GPIO.setup(self.PIN_DIR, GPIO.OUT)
              GPIO.output(self.PIN_DIR, CW)
              
              SPR_f = 50 # steps constituting to 11.25 degree rotation
              step_count = SPR_f
              for x in range(step_count):
                    GPIO.output(self.PIN_STEP, GPIO.HIGH)
                    time.sleep(delay)
                    GPIO.output(self.PIN_STEP, GPIO.LOW)
                    time.sleep(delay)
                    print('Rotating to change the marker from one frame to another')
                     
  def is_working(self):
    return self.working

  def stop_motor(self):
    #GPIO.setup(self.PIN_DIR, GPIO.LOW)
    print('Im inside stop_motor')
    #GPIO.setup(self.PIN_STEP, GPIO.LOW)
    #GPIO.cleanup() #correction here 1st
    self.running = False
    self.working = False
    sys.exit()
    #self.start_motor()