import requests

url ='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url=url, headers=headers)
print("Code status: {}".format(r.status_code))

response_dict = r.json()

print(response_dict.keys())
