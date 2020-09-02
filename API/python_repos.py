import requests

url ='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url=url, headers=headers)
print("Code status: {}".format(r.status_code))

response_dict = r.json()

print("Total number of repos: {}".format(response_dict['total_count']))

repo_dicts = response_dict['items']
print("Number of returned repos: {}".format(len(repo_dicts)))

repo_dict = repo_dicts[0]
# print("\nKeys: {}".format(len(repo_dict)))
# for key in sorted(repo_dict.keys()):
#     print(key)
for repo_dict in repo_dicts:
    print("\nSelected info about first repo: ")
    print("Name: {}".format(repo_dict['name']))
    print("Owner: {}".format(repo_dict['owner']['login']))
    print("Mark: {}".format(repo_dict['stargazers_count']))
    print("Repo: {}".format(repo_dict['html_url']))
    print("Description: {}".format(repo_dict['description']))
