import time

class Time_it:

    def __init__(self) -> None:
        self.set_neutral()

    def set_neutral(self):
        self.__start_time = 0
        self.__finish_time = 0
        self.__timed = False

    def start(self):
        self.__timed = True
        self.__start_time = time.time()
        
    def finish(self):
        self.__finish_time = time.time()

        res = self.__finish_time - self.__start_time if self.__timed else -1

        self.set_neutral()

        return res