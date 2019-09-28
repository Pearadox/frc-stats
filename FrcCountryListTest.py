import unittest
import FrcCountryList


def getTestData():
    return [];

class FrcCountryListTest(unittest.TestCase):

    def test_constructCountryCount(self):
        testInputData = getTestData();
        result = FrcCountryList.constructCountryCount(testInputData);
        self.assertEqual(0, 0);


if __name__ == '__main__':
    unittest.main()
