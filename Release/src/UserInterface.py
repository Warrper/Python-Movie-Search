from LocalStorage import LocalStorage
from Film import Film
import requests
import json

class UserInterface:
  def __init__(self):
    self.storage = LocalStorage()
  
  def Search_Films(self):
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
      Search_Films()
    
    validInput = False
    while validInput == False:
      saveFilm = input("\nWould you like to save this film? (y/n)\n> ")
      if saveFilm.lower() == "y":
        validInput = True
        self.Store_Film(filmObj)
      elif saveFilm.lower() == "n":
        validInput = True
  
  def Store_Film(self, filmObj):
    self.storage.Read_Films()
    if filmObj.Film_To_Dict() not in self.storage.films:
      self.storage.films.append(filmObj.Film_To_Dict())
    self.storage.Write_Films()

  
  def Edit_Storage(self):
    pass
  
  def View_Storage(self):
    pass