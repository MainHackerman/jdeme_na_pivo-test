import unittest
import sys
import os
#import project_test_inserted as project


class TestStaticVariables(unittest.TestCase):
    def test_pivo(self):
        pass
        #self.assertEqual(pivo, 80)


oldstdin = sys.stdin

try:
  from project import pivo
finally:
  sys.stdin = oldstdin

print(pivo)