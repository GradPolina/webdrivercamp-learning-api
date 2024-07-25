import requests
from pprint import pprint
def create_repo(url):
    data = {
        'name': 'repo-created-with-api',
        'private': True,
        'has_wiki': False
    }

    response = requests.post(url, json=data)
    print(f"Response status code: {response.status_code}")
    return response.json()


if __name__=='__main__':
    url = 'https://api.github.com/users/GradPolina/repos'
    repo = create_repo(url)
    pprint(repo)
