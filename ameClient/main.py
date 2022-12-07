import requests
import json

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
		if token is None or type(token) != str:
			raise TypeError("Token can not be None or not a str")
		self._token = token
		self.baseURL = "https://v1.api.amethyste.moe"

	def generate(self, endpoint, data = {}):
		"""
		Args:
			- endpoint: str
		"""
		if endpoint is None or type(endpoint) != str:
			raise TypeError("Endpoint can not be None or not a str")
		try:
			response = requests.request(method="POST",
							url=f"{self.baseURL}/generate/{endpoint}",
							data=data,
							headers={
							"Authorization": f"Bearer {self._token}"
							})
			if response.ok:
				return response.content
			else:
				response.raise_for_status()
		except Exception as e:
			raise e
	def get_generate_endpoints(self, premium=False):
		try:
			response = requests.request(method="GET",
										url=f"{self.baseURL}/generate",
										headers={
										"Authorization": f"Bearer {self._token}"
										})
			if response.ok:
				return json.loads(response.content)["endpoints"]["premium"] if premium else json.loads(response.content)["endpoints"]["free"]
			else:
				response.raise_for_status()
		except Exception as e:
			raise e
