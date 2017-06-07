"""\
Imposer
=======

Main promise class for use of barriers/shared states.
"""


class Imposer:
    def __init__(self, env):
        self.env = env
        return

    def resolve(self):
        """Notify the states are ready"""
        return

    def reject(self):
        """Notify its rejection with exceptions"""
        return

    def wait(self):
        """Block to wait for the returning states"""
        return

    def wait_for(self):
        """Wait but with a timeout"""
        return
