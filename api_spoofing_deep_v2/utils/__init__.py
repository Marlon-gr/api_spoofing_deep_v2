import sys
import time


def time_second():
    return time.time()


def time_count(_time):
    return round(time_second() - _time, 10)


def exc_info():
    type_, value, tb = sys.exc_info()
    return type_, value