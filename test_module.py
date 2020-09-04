import unittest
from convert_to_roman import convert_to_roman


# the test case
class UnitTests(unittest.TestCase):


    def test_arrangement_two(self):
        actual = convert_to_roman(2)
        expected = "II"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 2')



    def test_arrangement_three(self):
        actual = convert_to_roman(3)
        expected = "III"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 3')

        actual = convert_to_roman(3)
        expected = "III"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 3')


    def test_arrangement_four(self):
        actual = convert_to_roman(4)
        expected = "IV"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 4')



    def test_arrangement_five(self):
        actual = convert_to_roman(5)
        expected = "V"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 5')




    def test_arrangement_nine(self):
        actual = convert_to_roman(9)
        expected = "IX"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 9')




    def test_arrangement_twelve(self):
        actual = convert_to_roman(12)
        expected = "XII"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 12')



    def test_arrangement_sixteen(self):
        actual = convert_to_roman(16)
        expected = "XVI"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 16')


    def test_arrangement_twenty_nine(self):
        actual = convert_to_roman(29)
        expected = "XXIX"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 29')



    def test_arrangement_forty_four(self):
        actual = convert_to_roman(44)
        expected = "XLIV"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 45')


    def test_arrangement_forty_five(self):
        actual = convert_to_roman(45)
        expected = "XLV"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 45')

    def test_arrangement_sixty_eight(self):
        actual = convert_to_roman(68)
        expected = "LXVIII"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 68')


    def test_arrangement_eighty_three(self):
        actual = convert_to_roman(83)
        expected = "LXXXIII"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 83')

    def test_arrangement_nighnty_seven(self):
        actual = convert_to_roman(97)
        expected = "XCVII"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 97')

    def test_arrangement_nighnty_nine(self):
        actual = convert_to_roman(99)
        expected = "XCIX"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 99')

    def test_arrangement_four_hundred(self):
        actual = convert_to_roman(400)
        expected = "CD"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 500')

    def test_arrangement_five_hundred(self):
        actual = convert_to_roman(500)
        expected = "D"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 500')

    def test_arrangement_five_hundred_one(self):
        actual = convert_to_roman(501)
        expected = "DI"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 501')

    def test_arrangement_six_hundred_forty_nine(self):
        actual = convert_to_roman(649)
        expected = "DCXLIX"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 649')

    def test_arrangement_seven_hundred_ninety_eight(self):
        actual = convert_to_roman(798)
        expected = "DCXLIX"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 798')

    def test_arrangement_eight_hundred_ninety_one(self):
        actual = convert_to_roman(891)
        expected = "DCCCXCI"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 891')

    def test_arrangement_one_thousand(self):
        actual = convert_to_roman(1000)
        expected = "M"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 1000')

    def test_arrangement_one_thousand_four(self):
        actual = convert_to_roman(1004)
        expected = "MIV"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 1004')

    def test_arrangement_one_thousand_six(self):
        actual = convert_to_roman(1006)
        expected = "MVI"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 1006')

    def test_arrangement_one_thousand_twenty_three(self):
        actual = convert_to_roman(1023)
        expected = "MXXIII"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 1023')


    def test_arrangement_two_thousand_fourteen(self):
        actual = convert_to_roman(2014)
        expected = "MMXIV"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 2014')


    def test_arrangement_two_thousand_fourteen(self):
        actual = convert_to_roman(2014)
        expected = "MMXIV"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 2014')


    def test_arrangement_three_thousand_nine_hundred_nintey_nine(self):
        actual = convert_to_roman(3999)
        expected = "MMMCMXCIX"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "convert_to_roman()" with 3999')






if __name__ == "__main__":
    unittest.main()