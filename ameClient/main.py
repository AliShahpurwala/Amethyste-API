class ameClient:
	"""
	Class to create a connection to the Amethyste API
	"""

	def __init__(self, token, options = {}):
		"""
		Args:
			- token: str
			- options: Dict[Any, Any]
		Returns:
			- None
		Description:
			- Constructor for the ameClient class that requires a valid token string
		"""
		if token is None or type(token) != "str":
			raise TypeError("Token can not be None or not a str")
		self._token = token
		self.baseURL = "https://v1.api.amethyste.moe"

	def generate(endpoint, data = {}):
		pass