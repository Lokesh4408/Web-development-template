try:
    from .fake_gpio import GPIO # For running app
except ImportError:
    from fake_gpio import GPIO # For running main
    
#import RPi.GPIO as GPIO # For testing in Raspberry Pi

import time
from time import sleep 
import sys
import numpy as np

class SensorController:

  def __init__(self):
    self.PIN_TRIGGER = 18 # do not change
    self.PIN_ECHO = 24 # do not change
    self.distance = None
    self.color_from_distance = ""
    self.current_color = [False, False, False]
    print('Sensor controller initiated')
    
  def stop_sensor(self):
        sys.exit()

  def track_rod(self):
     #declaring number of measurements
        total_measurements = 20 #default is 20 but making it 2 for local machine
        distance_array = []

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(self.PIN_ECHO, GPIO.IN)
        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)
        #print ("Waiting for sensor to settle")
        time.sleep(1)
        
        for i in range(total_measurements):
            print ("Calculating distance")
            GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

            while GPIO.input(self.PIN_ECHO) == 0: pass
            self.pulse_start_time = time.time() #save start time
            while GPIO.input(self.PIN_ECHO) == 1: pass
            self.pulse_end_time = time.time() #save end time

            #pulse duration is calculated by subtraction between start and arrival     
            pulse_duration = self.pulse_end_time - self.pulse_start_time
            self.distance = round(pulse_duration * 17150, 2) #Half the speed (34300) due to bounce back
            print ("Distance:", self.distance, "cm")

            print('Monitoring')
            #distance_array = np.append(self.distance)
            distance_array.insert(i, self.distance)
            print('Current distance calculated for every iteration:', self.distance) #converting into cm
            self.distance = np.median(distance_array)   
            
            if int(self.distance) in range(4,9):
                self.color_from_distance = 'Yellow'
                self.current_color = [False, False, True]
            elif int(self.distance) in range(9,14):
                self.color_from_distance = 'Purple'
                self.current_color = [False, True, False]
            else:
                self.color_from_distance = 'Green'
                self.current_color = [True, False, False]        

  def get_distance(self):
      #self.track_rod()
      print('Current distance in cm:',self.distance)
      return self.distance

  def get_color_from_distance(self):
        #updating color_from_distance variable according to region before returning
        print(self.color_from_distance)
        print(self.current_color)
        return self.current_color
  
  