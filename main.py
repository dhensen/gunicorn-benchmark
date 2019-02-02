from time import sleep
from random import random

counter = 0


def app(environ, start_response):
    """Simplest possible application object"""
    # global counter
    # counter += 1
    # sleeptime = random() * 0.01
    # print(f'[{counter}] going under for {sleeptime}')
    # sleep(sleeptime)
    # print(f'[{counter}] waking up after {sleeptime}')
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(data)))]
    start_response(status, response_headers)
    return iter([data])
