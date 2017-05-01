#Movie Object Class
#Author: Soneer Sainion
#Example:
# m1 = Movie("I Am Legend", "Action, Drama", 2009)
# m1.getName()
class Movie:
   'Common base class for all movies'

   def __init__(self, name, list_genres, date):
      self.name = name
      self.list_genres = list_genres
      self.date = date

   def getName(self):
    return self.name
   
   def getGenres(self):
     return self.list_genres
   
   def getDate(self):
     return self.date
     

