import unittest
from random import randrange

from fatorial import fatorial, NotNaturalNumberError


class TestFatorial(unittest.TestCase):

	def test_fatorial_0(self):
		self.assertEqual(fatorial(0), 1)

	def test_fatorial_1(self):
		self.assertEqual(fatorial(1), 1)

	def test_fatorial_2(self):
		self.assertEqual(fatorial(2), 2)

	def test_fatorial_3(self):
		self.assertEqual(fatorial(3), 6)

	def test_fatorial_5(self):
		self.assertEqual(fatorial(5), 120)

	def test_fatorial_minus_1(self):
		with self.assertRaises(NotNaturalNumberError):
			fatorial(-1)

	def test_fatorial_negative(self):
		with self.assertRaises(NotNaturalNumberError):
			fatorial(randrange(-100,0))

	def test_fatorial_float(self):
		with self.assertRaises(NotNaturalNumberError):
			fatorial(randrange(1,100) / 10.0)


if __name__ == '__main__':
	unittest.main(verbosity=2)