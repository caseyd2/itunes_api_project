import requests

while True:
    search = input("Enter an artist or a song: ")

    url = "https://itunes.apple.com/search"

    params = {
        "term": search,
        "entity": "song",
        "limit": 5
}

    response = requests.get(url, params=params)

    if response.ok:
        data = response.json()

        if data["resultCount"] == 0:
            print("No Results Found")
        else:
            print("\nSearch Results:\n")
            for song in data["results"]:
                print("Song:", song["trackName"])
                print("Artist:", song["artistName"])
                print("Album:", song["collectionName"])
                print("Genre:", song["primaryGenreName"])
                print ()

    else: 
        print("There was an issue connecting to the API")

    again = input("Would you like to search again (y/n): ")

    if again.lower() != "y":
        print("Goodbye!")
        break
        


