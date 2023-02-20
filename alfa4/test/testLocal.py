import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from local import Local

class TestLocal(unittest.TestCase):
    def setUp(self):
        self.loc = Local()

    def test_words(self):
        #assuming that the file slovnik.txt has not been modified
        self.assertEqual(self.loc.dictionary["park"], "park")
        self.assertEqual(self.loc.dictionary["teenager"], "teenager")
        self.assertEqual(self.loc.dictionary["robot"], "robot")
        self.assertEqual(self.loc.dictionary["program"], "program")
        self.assertEqual(self.loc.dictionary["gang"], "gang")

        self.assertNotEqual(self.loc.dictionary["park"], "ahoj")
        self.assertNotEqual(self.loc.dictionary["gang"], "skola")


if __name__ == '__main__':
    unittest.main()
