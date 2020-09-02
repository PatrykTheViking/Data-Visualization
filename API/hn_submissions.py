from operator import itemgetter

import requests

url = "https://community-hacker-news-v1.p.rapidapi.com/topstories.json"

querystring = {"print": "pretty"}

headers = {
    'x-rapidapi-host': "community-hacker-news-v1.p.rapidapi.com",
    'x-rapidapi-key': "7fafa6c3c7mshe7f6176591e3223p1ca392jsnd6362f79993f"
    }

r = requests.get(url, headers=headers, params=querystring)
print("Status code: {}".format(r.status_code))

submissions_ids = r.json()
submissions_dicts = []
for submissions_id in submissions_ids[:5]:
    url = "https://community-hacker-news-v1.p.rapidapi.com/item/{}.json".format(submissions_id)

    querystring = {"print": "pretty"}

    headers = {
        'x-rapidapi-host': "community-hacker-news-v1.p.rapidapi.com",
        'x-rapidapi-key': "7fafa6c3c7mshe7f6176591e3223p1ca392jsnd6362f79993f"
        }

    r = requests.get(url, headers=headers, params=querystring)

    print("ID: {}\t STATUS: {}".format(submissions_id, r.status_code))
    response_dict = r.json()

    submission_dict = {
        'title': response_dict['title'],
        'url': response_dict['url'],
        'score': response_dict['score'],
    }

    submissions_dicts.append(submission_dict)

submissions_dicts = sorted(submissions_dicts, key=itemgetter('score'), reverse=True)

for submission_dict in submissions_dicts:
    print("Article title: {}". format(submission_dict['title']))
    print("URL: {}".format(submission_dict['url']))
    print("Score: {}". format(submission_dict['score']))
