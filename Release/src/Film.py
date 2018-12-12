class Film:
  def __init__(self, rDict):
    self.title = rDict["Title"]
    self.year = rDict["Year"]
    self.rating = rDict["Rated"]
    self.releaseDate = rDict["Released"]
    self.runtime = rDict["Runtime"]
    self.genre = rDict["Genre"]
    self.director = rDict["Director"]
    self.actors = rDict["Actors"]
    self.plot = rDict["Plot"]
    self.language = rDict["Language"]
    self.country = rDict["Country"]
    self.awards = rDict["Awards"]
  
  def Print_Info(self):
    print("Title: " + self.title)
    print("Year: " + self.year)
    print("Rated: " + self.rating)
    print("Released: " + self.releaseDate)
    print("Runtime: " + self.runtime)
    print("Genre: " + self.genre)
    print("Director: " + self.director)
    print("Actors: " + self.actors)
    print("Plot: " + self.plot)
    print("Language: " + self.language)
    print("Country: " + self.country)
    print("Awards: " + self.awards)

  def Film_To_Dict(self):
    out = {
        "Title": self.title,
        "Year": self.year,
        "Rated": self.rating,
        "Released": self.releaseDate,
        "Runtime": self.runtime,
        "Genre": self.genre,
        "Director": self.director,
        "Actors": self.actors,
        "Plot": self.plot,
        "Language": self.language,
        "Country": self.country,
        "Awards": self.awards
      }
    return out