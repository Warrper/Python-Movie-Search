from Film import Film
from LocalStorage import LocalStorage
import requests
import json

def Main():
  movieTitle = input("Please input a movie title\n> ")

  reqURL = 'http://www.omdbapi.com/?t=' + movieTitle.replace(" ", "+") + "&apikey=464fd173"

  r = requests.get(reqURL)
  rText = r.text
  rDict = json.loads(rText)

  try:
    filmObj = Film(rDict)
    filmObj.Print_Info()
  except:
    print("Enter a valid movie title\n")
    Main()
  
  store = LocalStorage()
  store.Read_Films()
  if (filmObj.Film_To_Dict() not in store.films):
    store.films.append(filmObj.Film_To_Dict())
  store.Write_Films()

Main()