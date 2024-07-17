import requests
from pprint import pprint
def create_repo(url):
    token = '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'
    headers = {
        'Authorization': f'Bearer {token}'}
    data = {
        'name': 'repo-created-with-api',
        'private': True,
        'has_wiki': False
    }

    response = requests.post(url, headers=headers, json=data)
    print(f"Response status code: {response.status_code}")
    return response.json()


if __name__=='__main__':
    url = 'https://api.github.com/user/repos'
    repo = create_repo(url)
    pprint(repo)
