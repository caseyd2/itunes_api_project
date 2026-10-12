import requests

search = input("Enter an artist or a song: ")

url = "https://itunes.apple.com/search"

params = {
    "term": search,
    "entity": "song",
    "limit": 20
}

response = requests.get(url, params=params)

data = response.json()

response = response.json()

if data["resultCount"] == 0:
    print("No Results Found")
else:
    for song in data["results"]:
        print("Song:", song["trackName"])
        print("Artist:", song["artistName"])
        print("Album:", song["collectionName"])
        print("Genre:", song["primaryGenreName"])
        print ()

    


