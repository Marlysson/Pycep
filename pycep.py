# -*- coding : utf-8 -*-

import requests
from models import CEP , Address

from exceptions import InvalidCepException, AddressNotFound

class PyCEP(object):

	URL_WEBSERVICE = "https://viacep.com.br/ws/{}/json/unicode/"

	@classmethod
	def get(cls,cep_value):

		cep = CEP(cep_value)

		number_cep = PyCEP.URL_WEBSERVICE.format(cep.value)

		request_to_cep = requests.get(number_cep).json()
		
		if "erro" in request_to_cep.keys():
			raise AddressNotFound("Address not found to this cep.")

		address_found = Address(request_to_cep)

		return address_found