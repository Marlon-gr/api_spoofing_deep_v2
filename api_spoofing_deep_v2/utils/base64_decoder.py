import base64

import cv2
import numpy as np


class Base64Decoder(object):
    """Image pre-processing.
    Decode base64 into image
    """
    def __call__(self, image):
        np_arr = np.frombuffer(base64.b64decode(image), np.uint8)
        return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)