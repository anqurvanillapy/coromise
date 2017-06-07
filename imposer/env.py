"""\
Env
===

Global or function local states for sync.
"""

import threading


class Env:
    def __init__(self):
        if not threading.current_thread() == threading.main_thread():
            raise RuntimeError('Env should be in the main thread')
