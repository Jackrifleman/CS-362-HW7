#Jackson Eubank
#CS362
#HW7 - Leap Year Testing

import unittest;
import leapyear;

class UnitTest(unittest.TestCase):
    def test_modulo_four(self):
        testNumb = leapyear.parseYear(4);
        self.assertEqual(testNumb,1);


if (__name__ == '__main__'):
    unittest.main();
