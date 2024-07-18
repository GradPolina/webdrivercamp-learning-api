import requests
def get_created_repo(url):
    headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/vnd.github+json'}
    response = requests.get(url, headers=headers)
    repo = response.json()

    assert repo['has_wiki'] == False
    assert repo['private'] == True
    assert repo['name'] == 'repo-created-with-api'
    assert repo['owner']['login'] == 'GradPolina'

    print(f"Response status code: {response.status_code}")
    return repo


if __name__=="__main__":
    url = "https://api.github.com/repos/GradPolina/repo-created-with-api"
    token = ''
    get_created_repo(url)
