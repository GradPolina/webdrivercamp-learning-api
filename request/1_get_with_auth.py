import requests
def get_with_auth(url):
    response = requests.get(url)
    print(f"Response status code {response.status_code}")
    repos = response.json()
    num_of_repos = len(repos)
    return num_of_repos, response.headers


if __name__=="__main__":
    url = 'https://api.github.com/users/GradPolina/repos'
    num_of_repos, headers = get_with_auth(url)
    print(f"Total Repos: {num_of_repos}")
    print(f"Response headers: {headers}")
