import requests

def search_repos(query):


    url = f"https://api.github.com/search/repositories?q={query}"


    response = requests.get(url, timeout=10)
    
    items = response.json()["items"][:3]

    return [
        {
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"]
        }
        for repo in items
    ]
