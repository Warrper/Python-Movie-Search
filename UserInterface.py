from LocalStorage import LocalStorage
from Film import Film
import requests
import json

class UserInterface:
  def __init__(self):
    self.storage = LocalStorage()

  def Interface_Options(self):
    usrQuit = False
    while usrQuit == False:
      print("\n" + ("-"*20) + "\n")
      userInput = input("1: Search for films\n2: View saved Films\n3: Edit saved Films\nq: Quit\n> ")
      if userInput == "1":
        self.Search_Films()
      elif userInput == "2":
        self.View_Storage()
      elif userInput == "3":
        self.Edit_Storage()
      elif userInput.lower() == "q":
        usrQuit = True
      else:
        print("Please Enter 1, 2, 3, or q\n")
  
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

  def Remove_Item(self):
    validInput = False
    while validInput == False:
      userInput = input("\nUse number to select the item you would like to remove from storage\nUse 'c' to cancel\n> ")
      if userInput.lower() == "c":
        break
      try:
        self.storage.films.pop(int(userInput))
        self.storage.Write_Films()
        validInput = True
        print("Item Removed")
      except:
        print("Item does not exist")
        validInput = False
  
  def Order_Items(self):
    validInput = False
    while validInput == False:
      userInput = input("\nUse number to select the item you would like to move\nUse 'c' to cancel\n> ")
      if userInput.lower() == "c":
        break
      else:
        try:
          item = self.storage.films.pop(int(userInput))
          validLocation = False
          while validLocation == False:
            moveLoc = input("Enter index where you want to insert the item\n> ")
            try:
              self.storage.films.insert(int(moveLoc), item)
              self.storage.Write_Films()
              self.View_Storage()
              validLocation = True
            except:
              print("Please enter a valid index")
              validLocation = False
          validInput = True
        except:
          print("Item does not exist.")



  def Edit_Storage(self):
    if self.View_Storage() == 0: #if storage is not empty
      validInput = False
      while validInput == False:
        userInput = input("\n1: Remove item from storage\n2: Change order of stored items\nc: Cancel\n> ")
        if userInput == "1":
          validInput = True
          self.Remove_Item()
        elif userInput == "2":
          validInput = True
          self.Order_Items()
        elif userInput.lower() == "c":
          validInput = True
  
  def View_Storage(self):
    self.storage.Read_Films()
    print("")
    if len(self.storage.films) > 0:
      for i in range(0, len(self.storage.films)):
        filmObj = Film(self.storage.films[i])
        print(str(i) + ": " + filmObj.title)
      return 0 
    else:
      print("No films currently in storage")
      return -1