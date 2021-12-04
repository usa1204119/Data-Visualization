import json
import pygal
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

# Group the countries in three categories
'''cc_pops_1 ,cc_pops_2 ,cc_pops_3 = {} ,{} ,{}
for cc,pop in cc_poulation.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop 
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

wm = pygal.maps.world.World()
wm.title = 'World Population in 2010 \n By Country'
wm.add('0-10m',cc_pops_1)
wm.add('10m-1b',cc_pops_2)
wm.add('<1b',cc_pops_3)

wm.render_to_file('world_population,2010.svg')
'''
cc_pops_1 , cc_pops_2 , cc_pops_3 = {} , {} , {}
for cc,pop in cc_poulations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

wm = pygal.maps.world.World()
wm.title = 'World Population in 2010 \n By Country'
wm.add('0-10m',cc_pops_1)
wm.add('10m-1b',cc_pops_2)
wm.add('>1b',cc_pops_3)
wm.render_to_file('world_population.svg')