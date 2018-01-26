# -*- coding: utf-8 -*-

import threading

class LineReader(threading.Thread):

    def __init__(self, pipe, queue):
        threading.Thread.__init__(self)
        self.src = pipe
        self.dst = queue
        self.daemon = True

    def run(self):
        for line in iter(self.src.readline, ''):
            self.dst.put(line)
