import requests
def update_repo(url):
    data = {'description': 'I know Python Requests!'}
    headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/vnd.github+json'}
    response = requests.patch(url, headers=headers, json=data)
    print(f"Response status code: {response.status_code}")
    return response.json()

if __name__=='__main__':
    url = 'https://api.github.com/repos/GradPolina/repo-created-with-api'
    token = ''
    repo = update_repo(url)
    assert repo['description'] == 'I know Python Requests!'
