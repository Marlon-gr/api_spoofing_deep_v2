import base64
import binascii
import logging
import os

import cv2
import numpy as np


def to_numpy(encoded):
    """Convert base64 to numpy.
    Args:
        encoded (str): Base64 encoded string to decode.
    Returns:
        :obj:`np.ndarray`: An ndimentional array of the input image.
    Raises:
        ValueError: Wrong base64 image.
    """
    nparr = np.frombuffer(base64.b64decode(encoded), np.uint8)
    try:
        np_res = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    except cv2.error:
        raise ValueError('No correct base64 value.')
    return np_res


def to_numpy_rgb(encoded):
    """Convert base64 to numpy.
    Args:
        encoded (str): Base64 encoded string to decode.
    Returns:
        :obj:`np.ndarray`: An ndimentional array of the input image.
    Raises:
        ValueError: Wrong base64 image.
    """
    nparr = np.frombuffer(base64.b64decode(encoded), np.uint8)
    try:
        np_res_rgb = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        np_res_rgb = cv2.cvtColor(np_res_rgb, cv2.COLOR_BGR2RGB)
    except cv2.error:
        raise ValueError('No correct base64 value.')
    return np_res_rgb


def is_base64(str_b64):
    """Check if str represents base64 format.
    Args:
        str_b64 (str): String containing base64 code.
    Returns:
        bool: True if input is base64 encoded, raise ValueError otherwise.
    Raises:
        ValueError: Wrong base64 input.
    """
    try:
        base64.b64decode(str_b64)
    except binascii.Error:
        raise ValueError('No correct base64 value.')
    return True


def environ_value(environ):
    """
    Get values from operating system environment.
    Args:
        environ: (str) Environment variable name.
    Returns:
        (str) Value of the environment variable.
    """
    try:
        value = os.environ[environ]
    except KeyError:
        logging.getLogger('spoofing.api').info(environ + ' > not found')
        value = True
    return value
