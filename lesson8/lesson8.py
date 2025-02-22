'''
import logging

logging.basicConfig(level = logging.DEBUG, filename="logs.log",
                    filemode="w",
                    format = "we have logging message: %(message)s - (levelname)s")



try:
    print(10/0)
except Exception:
    logging.exception("na 0 nelzaaaaa")
'''

'''
if 2+2 == 4:
    print("you are right")

assert 2+2 == 4
'''


"""
>>> 2+2
5
"""
'''
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    
    
    '''


import unittest
def add(a,b):
    return a+b

class TestMathAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 6)

if __name__ == "__main__":
    unittest.main()