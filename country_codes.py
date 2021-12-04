from pygal.maps.world import COUNTRIES

def get_country_codes(country_name):
	for code,name in COUNTRIES.items():
		if name == country_name:
			return code
		elif country_name == 'Yemen, Rep.':
			return 'ye'
		elif country_name == 'Qatar':
			return 'qa'
		elif country_name == 'Dominica':
			return 'do'
		elif country_name == 'Vietnam':
			return 'vn'
		# if country name not found return none
	print('Error:'+country_name)
	
