from Film import Film
from LocalStorage import LocalStorage
from UserInterface import UserInterface
import requests
import json

def Main():
  UI = UserInterface()

  UI.Search_Films()
  
  '''
  store = LocalStorage()
  store.Read_Films()
  if (filmObj.Film_To_Dict() not in store.films):
    store.films.append(filmObj.Film_To_Dict())
  store.Write_Films()
  '''

Main()