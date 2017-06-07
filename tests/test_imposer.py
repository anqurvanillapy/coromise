import unittest
import threading

import imposer

class TestBasic(unittest.TestCase):
    """Basic test cases of Env, Imposer"""
    def test_env_wrong_thread(self):
        """Test Env when running in the wrong thread"""
        def threadfn():
            """Env should be global"""
            with self.assertRaises(RuntimeError):
                env = imposer.Env()

        thr = threading.Thread(target=threadfn)
        thr.start()


if __name__ == '__main__':
    unittest.main()
