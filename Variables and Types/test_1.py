# from asserts import assert_true, assert_equal
import unittest
from unittest.mock import patch
from io import StringIO
class Test(unittest.TestCase):
    
    def test_begin_1(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            import begin_1
            actual = fake_output.getvalue().strip()
            self.assertEqual(actual, 'Hello World')