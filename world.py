import json
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes import get_country_codes
file_name = 'population_data.json'
with open(file_name) as f:
	pop_data = json.load(f)

cc_poulations = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_codes(country_name)
		if code:
			cc_poulations[code] = population
a,b,c = {},{},{}
for cc,pop in cc_poulations.items():
	if pop < 10000000:
		a[cc] = pop
	elif pop < 1000000000:
		b[cc] = pop
	else:
		c[cc] = pop

print(a)
wm_style = RS('#336699',base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010 \n By Country'
wm.add('0-10m',a)
wm.add('10m-1b',b)
wm.add('>1b',c)
wm.render_to_file('world.svg')
