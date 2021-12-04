import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_dicts = r.json()
print('Status Code :',r.status_code)
repo_dicts = response_dicts['items']
# Examine the first repository
names,plot_dicts = [],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	plot_dict = {
	'value':repo_dict['stargazers_count'],
	'label':repo_dict['description'] or "",
	'xlink':repo_dict['html_url'],
	}
	plot_dicts.append(plot_dict)
my_style = LS('#336699',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000 
chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most starred python projects on github'
chart.x_labels = names
chart.add('',plot_dicts)
chart.render_to_file('python_repo.svg')