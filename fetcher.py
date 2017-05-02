# Fetcher Class
# Author: Wai Myint


import requests
import apikey as api
import movie

class Fetcher:
    count = 0
    genresT = []

    def __init_(self):
        self.count = 0

    def fetch(self, movieList, a=1):
        if movieList is None:
            return False

        response = requests.get(api.base + "movie/now_playing" + api.v3 + api.end)
        if response.status_code == 200:
            data = response.json()
            if self.count < data['total_results']:
                for x in range(0, a):
                    name = data['results'][self.count]['title']
                    genres = []
                    for y in data['results'][self.count]['genre_ids']:
                        gName = (b for b in api.genre if b['id'] == y).next()['name']
                        genres.append(gName)
                        if gName not in self.genresT:
                            self.genresT.append(gName)
                    date = data['results'][self.count]['release_date']
                    m = movie.Movie(name, genres, date)
                    movieList.append(m)
                    self.count += 1

                    print "fetch successful, # of movies in the list: " +str(self.count)
                    print " # of genres: " +str(len(self.genresT))
            else:
                print "Cannot fetch anymore new movies, no more in existent"
        else:
            print "API fetch failed, try again"
            return False

    def printMovieList(self, movieList):
        for x in movieList:
            print "Movie: " + x.getName() + "\n Genre: " + ', '.join(
                x.getGenres()) + "\n  Release Date: " + x.getDate() + "\n"

    def printGenres(self):
        print "Total Genres: " + str(len(self.genresT)) + ""
        print "Genres: " + ', '.join(self.genresT)


movieList = []
f = Fetcher()
f.fetch(movieList, 3)
f.fetch(movieList, 10)

f.printMovieList(movieList)
f.printGenres()

