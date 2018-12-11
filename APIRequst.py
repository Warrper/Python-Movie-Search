import requests
import json

def Movie_Search():
  movieTitle = input("Please input a movie title\n> ")

  reqURL = 'http://www.omdbapi.com/?t=' + movieTitle.replace(" ", "+") + "&apikey=464fd173"

  r = requests.get(reqURL)
  rText = r.text
  rDict = json.loads(rText)

  try:
    print("Title: " + rDict["Title"])
    print("Year: " + rDict["Year"])
    print("Rated: " + rDict["Rated"])
    print("Released: " + rDict["Released"])
    print("Runtime: " + rDict["Runtime"])
    print("Genre: " + rDict["Genre"])
    print("Director: " + rDict["Director"])
    print("Actors: " + rDict["Actors"])
    print("Plot: " + rDict["Plot"])
    print("Language: " + rDict["Language"])
    print("Country: " + rDict["Country"])
    print("Awards: " + rDict["Awards"])
  except:
    print("Please enter a valid move title\n")
    Movie_Search()
Movie_Search()