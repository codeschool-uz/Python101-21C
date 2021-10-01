import unittest
from func_hi import hi

class Test(unittest.TestCase):

    def test_func_hi(self):
        output = hi()
        actual = 'hello'
        self.assertEqual(actual, output)

 
  