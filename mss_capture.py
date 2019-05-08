import time
import numpy as np
import cv2
import mss
from PIL import Image
def abc():
  with mss.mss() as sct:
    monitor = {'top': 146, 'left': 1911, 'width': 400, 'height': 220}

    last_time = time.time()

    img = np.array(sct.grab(monitor))
    #print("in_mss")

    return img
