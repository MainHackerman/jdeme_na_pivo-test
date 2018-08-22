import unittest
import project

class TestStaticVariables(unittest.TestCase):
    def test_pivo(self):
        self.assertEqual(project.pivo, 80)

    def