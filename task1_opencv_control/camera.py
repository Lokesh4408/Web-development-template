# Please note that this is a fake camera, it will just 
# yield the images 1.jpg, 2.jpg, 3.jg and 4.jpg. It is
# just for testing purposes. You should actually use the
# picamera module and implement the get_frame properly  

import os
from time import time


class Camera(object):
    def __init__(self):
        directory = os.path.join(os.path.dirname(__file__), 'test_frames')
        self.test_frames_name = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
        self.frames = [open(os.path.join(directory, f), 'rb').read() for f in self.test_frames_name]
        self.current_frame = int(time()) % 4
        self.count = 0

    def get_frame(self):
        if self.count > 20: #2000
            self.current_frame = int(time()) % 4
            self.count = 0
        index = int(time()) % 4
        print('Frame', self.test_frames_name[self.current_frame])
        self.count = self.count + 1
        #jpg_as_np = np.fromstring(self.current_frame, np.uint8)
        #img = cv2.imdecode(jpg_as_np, cv2.COLOR_BGR2RGB)
        return self.frames[self.current_frame]
