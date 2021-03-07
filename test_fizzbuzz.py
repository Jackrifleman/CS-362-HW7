#Jackson Eubank
#CS362
#HW7 - FizzBuzz Testing

import unittest;
import fizzbuzz;

class UnitTest(unittest.TestCase):
    def test_regular_number(self):
        testNumb = fizzbuzz.parseNumb(4);
        self.assertEqual(testNumb,"4");

    


if (__name__ == '__main__'):
    unittest.main();
