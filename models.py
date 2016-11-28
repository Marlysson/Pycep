# -*- coding : utf-8 -*-

import re
from exceptions import InvalidCepException

REGEX_CEP = r"^\d{5}-?\d{3}$"

class CEP(object):
	
	def __init__(self,value):
		self.value = self._normalized(value)

		self._validate()

	def _validate(self):
		if not re.match(REGEX_CEP,self.value):
			raise InvalidCepException("Invalid cep")

	def _normalized(self,value):

		'''
		Normalizing cep value
		'''

		value = value.replace("-","")
		return value