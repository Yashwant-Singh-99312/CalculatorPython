import unittest
import sys
sys.path.append("app")
from Calculator import Calculator


class TestCalculator(unittest.TestCase):

    def testSumaCorrecta(self):
        calc = Calculator()
        self.assertEqual(4, calc.suma(2, 2))

    def testSumaNegativos(self):
        calc = Calculator()
        self.assertEqual(-4, calc.suma(-2, -2))

    def testRestaCorrecta(self):
        calc = Calculator()
        self.assertEqual(2, calc.resta(4, 2))

    def testRestaNegativos(self):
        calc = Calculator()
        self.assertEqual(0, calc.resta(-2, -2))

    def testMultipliacionCorrecta(self):
        calc = Calculator()
        self.assertEqual(8, calc.multiplicar(4, 2))

    def testMultiplicacionNegativos(self):
        calc = Calculator()
        self.assertEqual(-16, calc.multiplicar(8, -2))

    def testDivisionCorrecta(self):
        calc = Calculator()
        self.assertEqual(4, calc.dividir(8, 2))

    def testDivisionNegativo(self):
        calc = Calculator()
        self.assertEqual(2, calc.dividir(-8, -4))
if __name__ == '__main__':
    unittest.main()
