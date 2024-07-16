import requests
def get_with_auth(url):
    token = "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"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    print(f"Response status code {response.status_code}")
    repos = response.json()
    return len(repos), response.headers





if __name__=="__main__":
    url = "https://api.github.com/user/repos"
    num_of_repos, headers = get_with_auth(url)
    print(f"Total Repos: {num_of_repos}")
    print(f"Response headers: {headers}")
