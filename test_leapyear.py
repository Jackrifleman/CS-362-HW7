#Jackson Eubank
#CS362
#HW7 - Leap Year Testing

import unittest;
import leapyear;

class UnitTest(unittest.TestCase):
    def test_modulo_four(self):
        testNumb = leapyear.parseYear(4);
        self.assertEqual(testNumb,1);
    def test_modulo_hundred(self):
        testNumb = leapyear.parseYear(104);
        self.assertEqual(testNumb,0);


if (__name__ == '__main__'):
    unittest.main();
