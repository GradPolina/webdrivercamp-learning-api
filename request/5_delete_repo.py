import requests
def delete_repo(url):
    headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/vnd.github+json'}
    response = requests.delete(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    return response.json()
if __name__=="__main__":
    url = f'https://api.github.com/repos/GradPolina/repo-created-with-api'
    token = ''
    delete_repo(url)
