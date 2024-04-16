import time

class __Time_it:

    def __init__(self) -> None:
        self.__set_neutral()

    def __set_neutral(self):
        self.__start_time = 0
        self.__finish_time = 0
        self.__timed = False

    def start(self):
        self.__timed = True
        self.__start_time = time.time()
        
    def finish(self):
        self.__finish_time = time.time()

        res = self.__finish_time - self.__start_time if self.__timed else -1

        self.__set_neutral()

        return res
    
__timer = __Time_it()

def start():
    __timer.start()

def finish():
    return __timer.finish()