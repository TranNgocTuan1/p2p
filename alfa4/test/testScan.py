import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from scan import Scan

class TestScan(unittest.TestCase):
    def setUp(self):
        self.scan = Scan()

    def test_ips(self):
        #assuming that ipAporty.txt contains ip range 10.0.1.20-10.0.1.21
        self.assertEqual(str(self.scan.firstIP), "10.0.1.20")
        self.assertEqual(str(self.scan.lastIP), "10.0.1.21")

    def test_ports(self):
        #assuming that ipAporty.txt contains ports range 65532-65533
        self.assertEqual(self.scan.firstPort, 65532)
        self.assertEqual(self.scan.lastPort, 65533)

if __name__ == '__main__':
    unittest.main()