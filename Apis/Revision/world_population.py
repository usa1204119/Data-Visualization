import csv
import json
import pygal.maps.world
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
from country_codes import get_country_codes
# Load the data into the list
file_name = 'world_population.json'
with open(file_name) as f:
	pop_data = json.load(f)
cc_population = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_codes(country)
		if code:
			cc_population[code] = population
		else:
			print('Error:'+country)
cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}

for cc,pop in cc_population.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop 
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
wm_style = RS('#336699')
wm = pygal.maps.world.World(style=wm_style,base_style=LCS)
wm.title = 'World Population in  2010'
wm.add('0-10m',cc_pops_1)
wm.add('10m-1b',cc_pops_2)
wm.add('>1b',cc_pops_3)

wm.render_to_file('world.svg')