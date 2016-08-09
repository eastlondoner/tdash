import time

class Stopwatch(object):
    def __init__(self, inside_mg='Default watch,'):
        self.start_time = time.time()
        self.inside_mg = inside_mg

    def print_time(self, msg):
        print self.inside_mg, 'Time: ', msg, ':   ', time.time() - self.start_time
        self.start_time = time.time()