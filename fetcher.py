# Fetcher Class
# Author: Wai Myint


import requests
import apikey as api
import movie

class Fetcher:

    popular = 0
    theater = 0
    genresT = []

    def __init_(self):
        self.theater = 0
        self.popular = 0

    def fetch(self, movieList, a=1, type='theater'):
        if movieList is None:
            return False

        if type is 'theater':
            type = self.theater
        else:
            type = self.popular

        if type is self.theater:
            response = requests.get(api.base + api.theater + api.v3 + api.end)
        else:
            response = requests.get(api.base + api.popular + api.v3 + api.end)

        if response.status_code == 200:
            data = response.json()
            if type < data['total_results']:
                for x in range(0, a):
                    name = data['results'][type]['title']
                    genres = []
                    for y in data['results'][type]['genre_ids']:
                        gName = (b for b in api.genre if b['id'] == y).next()['name']
                        genres.append(gName)
                        if gName not in self.genresT:
                            self.genresT.append(gName)
                    date = data['results'][type]['release_date']
                    m = movie.Movie(name, genres, date)
                    movieList.append(m)
                    type += 1

                    #print "fetch successful, # of movies in the list "+str(type) +""
                    #print " # of genres: " +str(len(self.genresT))
            else:
                print "Cannot fetch anymore new movies, no more in existent"
                return False
                
        else:
            pass

    def printMovieList(self, movieList):
        for x in movieList:
            print "Movie: " + x.getName() + "\n Genre: " + ', '.join(
                x.getGenres()) + "\n  Release Date: " + x.getDate() + "\n"

    def printGenres(self):
        print "Total Genres: " + str(len(self.genresT)) + ""
        print "Genres: " + ', '.join(self.genresT)


popular = []
theater = []
f = Fetcher()

""" fetch(movieList Object, # of movies to fetch, 'popular' or 'theater')"""
#f.fetch(popular, 3, 'popular')
#f.fetch(theater, 4, 'theater')

f#.printMovieList(popular)

#f.printMovieList(theater)
#f.printGenres()

