import unittest
from roman import roman

class TestRoman(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(roman(1), "I")

    def test_2(self):
        self.assertEqual(roman(2), "II")
    
    def test_3(self):
        self.assertEqual(roman(3), "III")
    
    def test_4(self):
        self.assertEqual(roman(4), "IV")
        
    def test_5(self):
        self.assertEqual(roman(5), "V")        

    def test_6(self):
        self.assertEqual(roman(6), "VI")

    def test_8(self):
        self.assertEqual(roman(8), "VIII")

    def test_9(self):
        self.assertEqual(roman(9), "IX")

    def test_10(self):
        self.assertEqual(roman(10), "X")

    def test_12(self):
        self.assertEqual(roman(12), "XII")
    
    def test_14(self):
        self.assertEqual(roman(14), "XIV")
        
    def test_15(self):
        self.assertEqual(roman(15), "XV")

    def test_18(self):
        self.assertEqual(roman(18), "XVIII")
                                
    def test_19(self):
        self.assertEqual(roman(19), "XIX")

    def test_22(self):
        self.assertEqual(roman(22), "XXII")

    def test_34(self):
        self.assertEqual(roman(34), "XXXIV")

    def test_40(self):
        self.assertEqual(roman(40), "XL")

    def test_49(self):
        self.assertEqual(roman(49), "XLIX")

    def test_50(self):
        self.assertEqual(roman(50), "L")

    def test_88(self):
        self.assertEqual(roman(88), "LXXXVIII")

    def test_90(self):
        self.assertEqual(roman(90), "XC")

    def test_96(self):
        self.assertEqual(roman(96), "XCVI")

    def test_100(self):
        self.assertEqual(roman(100), "C")

    def test_216(self):
        self.assertEqual(roman(216), "CCXVI")                

    def test_400(self):
        self.assertEqual(roman(400), "CD")

    def test_404(self):
        self.assertEqual(roman(404), "CDIV")

    def test_500(self):
        self.assertEqual(roman(500), "D")

    def test_666(self):
        self.assertEqual(roman(666), "DCLXVI")

    def test_900(self):
        self.assertEqual(roman(900), "CM")
        
    def test_1000(self):
        self.assertEqual(roman(1000), "M")        

    def test_3888(self):
        self.assertEqual(roman(3888), "MMMDCCCLXXXVIII")            

if __name__ == '__main__':
    unittest.main()