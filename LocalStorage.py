import json
class LocalStorage:
  def __init__(self):
    self.films = []
  
  def Read_Films(self):
    try:
      f = open("films.json", "r")
      try:
        x = json.loads(f.read())
        self.films = x
      except:
        pass
    except:
      print("File does not exist.")
  
  def Write_Films(self):
    #create file if not exist
    f = open("films.json", "w")
    #append to file
    f = open("films.json", "a")
    f.write(json.dumps(self.films, indent=2))