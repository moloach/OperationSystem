"""
This script runs the emailuoOperationSystem application using a development server.
"""

from thread import start_new_thread
from os import environ
from emailuoOperationSystem import app
from emailuoOperationSystem.check_server import start_check

def print_func():
    print 'im working'


if __name__ == '__main__':

    start_new_thread(start_check,())
    
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        #PORT = 5000
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.debug = True

    app.run(HOST, PORT)
