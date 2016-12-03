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
			raise InvalidCepException("Invalid cep, must be string with ou without separator")

	def _normalized(self,value):

		try:
			value = value.replace("-","")
		except AttributeError:
			raise InvalidCepException("Invalid cep, must be string with ou without separator")		

		return value


class Address(object):

	def __init__(self,data):

		self.cep = data["cep"]
		self.logradouro = data["logradouro"]
		self.complemento = data["complemento"]
		self.bairro = data["bairro"]
		self.localidade = data["localidade"]
		self.uf = data["uf"]
		self.unidade = data["unidade"]
		self.ibge = int(data["ibge"])
		self.gia = int(data["gia"]) if data["gia"] else data["gia"]