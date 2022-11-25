from unittest import TestCase, main
from Unittest import calc

class CalcTest( TestCase):
    def test_plus(self):
        self.assertEqual(calc('2+2'),4)
    def test_minus(self):
        self.assertEqual(calc('3-2'),1)
    def test_mult(self):
        self.assertEqual(calc('3*2'),6)
    def test_divide(self):
        self.assertEqual(calc('4/2'),2)    
    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('flvnfkvn')
        self.assertEqual('Хоть один знак', e.exception.args[0])

    def test_two_signs(self):
            with self.assertRaises(ValueError) as e:
                calc('4+4+4')
            self.assertEqual('Need 2 numbers and 1 sign', e.exception.args[0])

    def test_many_signs(self):
            with self.assertRaises(ValueError) as e:
                calc('4*4+4')
            self.assertEqual('Need 2 numbers and 1 sign', e.exception.args[0])
    def test_no_signs(self):
            with self.assertRaises(ValueError) as e:
                calc('2.4+1.0')
            self.assertEqual('Need 2 numbers and 1 sign', e.exception.args[0])
    def test_two_strings(self):
            with self.assertRaises(ValueError) as e:
                calc('a+b')
            self.assertEqual('Need 2 numbers and 1 sign', e.exception.args[0])


if __name__=="__main__":
    main()