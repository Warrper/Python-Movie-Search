import json
class LocalStorage:
  def __init__(self):
    self.films = []
  
  def ReadFilms(self, directory):
    print("Does Nothing")
  
  def WriteFilms(self):
    #create file if not exist
    f = open("films.txt", "w")
    #append to file
    f = open("films.txt", "a")
    temp = list()
    for i in range(len(self.films)):
      temp.append ({
        "Title": self.films[i].title,
        "Year": self.films[i].year,
        "Rated": self.films[i].rating,
        "Released": self.films[i].releaseDate,
        "Runtime": self.films[i].runtime,
        "Genre": self.films[i].genre,
        "Director": self.films[i].director,
        "Actors": self.films[i].actors,
        "Plot": self.films[i].plot,
        "Language": self.films[i].language,
        "Country": self.films[i].country,
        "Awards": self.films[i].awards
      })
    f.write(json.dumps(temp, indent=2))