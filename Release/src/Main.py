from Film import Film
from LocalStorage import LocalStorage
from UserInterface import UserInterface
import requests
import json

def Main():
  UI = UserInterface()
  UI.Search_Films()
Main()