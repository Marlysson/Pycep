# -*- coding : utf-8 -*-

import unittest

from exceptions import InvalidCepException
from models import CEP

class TestCEPFormat(unittest.TestCase):

	def test_cep_must_be_right_format(self):
		
		format_cep = CEP("00000111")

	def test_cep_must_be_wrong_format(self):

		with self.assertRaises(InvalidCepException):
			format_cep = CEP('231')

	def test_must_return_your_value_normalized(self):

		cep = CEP("12345-678")

		self.assertEqual("12345678",cep.normalized)

	def test_must_return_your_value_normalized_without_separator(self):
		cep = CEP("12363378")

		self.assertEqual("12363378",cep.normalized)

if __name__ == "__main__":
	unittest.main(verbosity=2)