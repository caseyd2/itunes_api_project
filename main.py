import requests

search = input("Enter an artist or a song: ")

url = "https://itunes.apple.com/search"

params = {
    "term": search,
    "entity": "song",
    "limit": 5
}

response = requests.get(url, params=params)

print(response.status_code)

