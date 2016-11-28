
class PycepException(Exception):
	pass

class AddressNotFound(PycepException):
	def __init__(self,message):
		self.message = message

class InvalidCepException(PycepException):
	def __init__(self,message):
		self.message = message
