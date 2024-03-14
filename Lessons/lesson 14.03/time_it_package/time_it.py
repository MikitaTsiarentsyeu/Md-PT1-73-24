"""this is a module to calculate running time"""

import time

start_time = None
is_started = False

def start():
    global start_time
    global is_started
    start_time = time.time()
    is_started = True
    return start_time

def finish():
    global is_started
    if is_started:
        end_time = time.time()
        is_started = False
        return end_time - start_time