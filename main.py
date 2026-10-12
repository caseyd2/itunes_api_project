import requests

while True:
    search = input("Enter an artist or a song: ")

    if search.lower() == "quit":
        print("Goodbye!")
        break 

    url = "https://itunes.apple.com/search"

    params = {
        "term": search,
        "entity": "song",
        "limit": 20
}

    response = requests.get(url, params=params)

    if response.ok:
        data = response.json()

        if data["resultCount"] == 0:
            print("No Results Found")
        else:
            for song in data["results"]:
                print("Song:", song["trackName"])
                print("Artist:", song["artistName"])
                print("Album:", song["collectionName"])
                print("Genre:", song["primaryGenreName"])
                print ()

    else: 
        print("There was an issue connecting to the API")
        


