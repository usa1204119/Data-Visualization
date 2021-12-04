import json
import pygal.maps.world
from country_codes import get_country_codes
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

file_name = 'gdp.json'
with open(file_name) as f:
	gdp_data = json.load(f)

cc_gdp = {}
for gdp_dict in gdp_data:
	if gdp_dict['Year'] == 2016:
		country = gdp_dict['Country Name']
		gdp_val = int(float(gdp_dict['Value']))
		code = get_country_codes(country)
		if code:
			cc_gdp[code] = gdp_val
		

cc_gdp_1,cc_gdp_2,cc_gdp_3 = {},{},{}
for cc,gdp in cc_gdp.items():
	if gdp < 5000000000:
		cc_gdp_1[cc] = round(gdp/1000000000)
	elif gdp < 50000000000:
		cc_gdp_2[cc] = round(gdp/1000000000)
	else:
		cc_gdp_3[cc] = round(gdp/1000000000)
print(len(cc_gdp_1),len(cc_gdp_2),len(cc_gdp_3))

wm_style = RS('#336699',base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'GDP 2016'
wm.add('0-5b',cc_gdp_1)
wm.add('5b-50b',cc_gdp_2)
wm.add('>50b',cc_gdp_3)
wm.render_to_file('gdp_index.svg')