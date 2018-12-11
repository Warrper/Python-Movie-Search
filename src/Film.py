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