import json
import pygal.maps.world
from country_codes import get_country_codes
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
with open('global_gdp.json') as f:
	gdp_data = json.load(f)

global_gdp = {}
for gdp_dict in gdp_data:
	if gdp_dict['Year'] =='2014':
		country_name = gdp_dict['Country Name']
		total_gdp = int(float(gdp_dict['Value']))
		code = get_country_codes(country_name)
		if code:
			global_gdp[code] = total_gdp

cc_gdps_1,cc_gdps_2,cc_gdps_3 = {},{},{}
for cc,gdp in global_gdp.items():
	if gdp < 5000000000:
		cc_gdps_1[cc] = round(gdp/1000000000)
	elif gdp < 50000000000:
		cc_gdps_2[cc] = round(gdp/1000000000)
	else:
		cc_gdps_3[cc] = round(gdp/1000000000)

print(len(cc_gdps_1),len(cc_gdps_2),len(cc_gdps_3))
wm_style = RS('#336699',base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'GDP 2014 \n By Country(In Billion Usd)'
wm.add('0-5b',cc_gdps_1)
wm.add('5bn-50bn',cc_gdps_2)
wm.add('>50bn',cc_gdps_3)

wm.render_to_file('gdp.svg')