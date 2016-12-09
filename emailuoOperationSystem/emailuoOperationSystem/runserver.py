"""
This script runs the emailuoOperationSystem application using a development server.
"""

from thread import start_new_thread
from os import environ
from emailuoOperationSystem import app


if __name__ == '__main__':
    
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        #PORT = 5000
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.debug = True

    app.run(HOST, PORT)
