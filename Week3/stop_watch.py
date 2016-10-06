import time


class StopWatch(object):

    def __init__(self):
        pass

    def starta(self):
        self.start = time.time() * 1000


    def stopa(self):
        self.stop = time.time() * 1000

    def get_elapsed_time(self, bericht = "Tijd: "):
        time = self.stop - self.start
        return bericht, time

