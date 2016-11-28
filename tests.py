# -*- coding : utf-8 -*-

import unittest

from exceptions import AddressNotFound, InvalidCepException 
from models import CEP , Address
from pycep import PyCEP as pycep

class TestCEPFormat(unittest.TestCase):

	def test_cep_must_be_right_format(self):
		
		format_cep = CEP("00000111")

	def test_cep_must_be_wrong_format(self):

		with self.assertRaises(InvalidCepException):
			format_cep = CEP("999999999")

	def test_cep_must_be_wrong_with_separator(self):

		with self.assertRaises(InvalidCepException):
			format_cep = CEP("99999-9999")

	def test_must_return_your_value_normalized(self):

		cep = CEP("12345-678")

		self.assertEqual("12345678",cep.value)

	def test_must_return_your_value_normalized_without_separator(self):
		cep = CEP("12363378")

		self.assertEqual("12363378",cep.value)


		
class TestWrapperBehaviorRequestAPI(unittest.TestCase):

	def test_wrapper_must_raise_exception_with_cep_is_wrong_format(self):

		with self.assertRaises(InvalidCepException):
			cep = pycep.get("999999999")
		
	def test_wrapper_must_raise_exception_when_cep_is_not_found(self):

		with self.assertRaises(AddressNotFound):
			cep = pycep.get("99999999")
		
	def test_wrapper_must_return_object_address_by_request_right(self):

		address = pycep.get("01001000")

		self.assertIsInstance(address,Address)


if __name__ == "__main__":
	unittest.main(verbosity=2)