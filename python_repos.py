import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status Code:',r.status_code)

response_dict = r.json()
print(response_dict.keys())
print('Total repositories :',response_dict['total_count'])

# Explore the information about the repositories
repo_dict = response_dict['items']
print('Repositories Returned : ',len(repo_dict))