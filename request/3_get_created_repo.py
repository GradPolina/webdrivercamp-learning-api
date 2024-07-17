import requests
def get_created_repo(url):
    token = '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'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url.format(owner='GradPolina', repo='repo-created-with-api'), headers=headers)
    repo = response.json()

    assert repo['has_wiki'] == False
    assert repo['private'] == True
    assert repo['name'] == 'repo-created-with-api'
    assert repo['owner']['login'] == 'GradPolina'

    print(f"Response status code: {response.status_code}")
    return repo


if __name__=="__main__":
    url = "https://api.github.com/repos/{owner}/{repo}"
    get_created_repo(url)
