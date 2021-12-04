import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
# make an api call and store the requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status Code : ',r.status_code)

# store the api response in a variable
response = r.json()
print('Total Repositories :',response['total_count'])

# explore the information about the repositories
repo_dicts = response['items']

names,plot_dicts = [],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	plot_dict = {
		'value':repo_dict['stargazers_count'],
		'label':repo_dict['description'] or "",
		'xlink':repo_dict['html_url'],
		}
	plot_dicts.append(plot_dict)

# make visualization
my_style = LS('#716699',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 28
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-starred python projects on github'
chart.x_labels = names 

chart.add(' ',plot_dicts)
chart.render_to_file('python_repos.svg')
