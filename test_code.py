import unittest
import sys
import io

oldstdin, sys.stdin = sys.stdin, io.StringIO('10\n100\nPepa\n5')

try:
  from project import pivo
finally:
  sys.stdin = oldstdin

class TestStaticVariables(unittest.TestCase):
    def test_pivo(self):
        pass
        #self.assertEqual(pivo, 80)




print(pivo)