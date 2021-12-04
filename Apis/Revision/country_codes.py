from pygal.maps.world import COUNTRIES
def get_country_codes(country_name):
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code 
		elif country_name == 'Yemen, Rep.':
			return 'ye'
		
	return None

