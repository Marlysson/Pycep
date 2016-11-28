# -*- coding : utf-8 -*-

import re
from exceptions import InvalidCepException

REGEX_CEP = r"\d{5}-?\d{3}"

class CEP(object):
	
	def __init__(self,value):
		self.value = value

		self._validate()

	def _validate(self):
		if not re.match(REGEX_CEP,self.value):
			raise InvalidCepException("Invalid cep")
		

	@property
	def normalized(self):

		'''
		Normalizing cep value
		'''

		value = self.value.replace("-","")
		return value
