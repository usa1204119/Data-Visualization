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

names,stars = [],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

# make visualization
my_style = LS('#336699',base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend = False)
chart.title = 'Most-starred python projects on github'
chart.xlabel = names 

chart.add('',stars)
chart.render_to_file('python_repos.svg')