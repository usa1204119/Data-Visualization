import unittest
from country_codes import get_country_codes
class TestCountryCodes(unittest.TestCase):
	def test_get_country_codes(self):
		code = get_country_codes('India')
		self.assertEqual(code,'in')
unittest.main()