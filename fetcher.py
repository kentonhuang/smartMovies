# Fetcher Class
# Author: Wai Myint


import requests
import apikey as api
import movie

class Fetcher:

    popular = 0
    popular_page = 1
    theater = 0
    theater_page = 1
    genresT = []

    def __init_(self):
        self.theater = 0
        self.popular = 0

    def fetch(self, movieList, a=1, type='theater'):
        if movieList is None:
            return False


        if type is 'theater':
            response = requests.get(api.base + api.theater + api.v3 + api.end + str(self.theater_page))
            ct = self.theater
        else:
            response = requests.get(api.base + api.popular + api.v3 + api.end + str(self.popular_page))
            ct = self.popular
        if response.status_code == 200:
            data = response.json()
        else:
            print "API fetch error"
            return False

        x = 0
        while x < a:
            if ct < len(data['results']):
                name = data['results'][ct]['original_title']
                genres = []
                for y in data['results'][ct]['genre_ids']:
                    gName = (b for b in api.genre if b['id'] == y).next()['name']
                    genres.append(gName)
                    if gName not in self.genresT:
                        self.genresT.append(gName)
                date = data['results'][ct]['release_date']
                m = movie.Movie(name, genres, date)
                movieList.append(m)
                if type is 'theater':
                    self.theater += 1
                else:
                    self.popular += 1
                ct += 1
                x += 1
                ##print "fetch successful, # of movies in the list "+str(type) +""
                #print " # of genres: " +str(len(self.genresT))
            else:
                if type is 'theater':
                    if self.theater_page > data['total_pages']:
                        print "Cannot pull anymore movies from theater"
                        return False
                    self.theater_page += 1
                    self.theater = 0
                    response = requests.get(api.base + api.theater + api.v3 + api.end + str(self.theater_page))
                    ct = self.theater
                else:
                    if self.popular_page > data['total_pages']:
                        print "Cannot pull anymore movies from theater"
                        return False
                    self.popular_page += 1
                    self.popular = 0
                    response = requests.get(api.base + api.popular + api.v3 + api.end + str(self.popular_page))
                    ct = self.popular
                if response.status_code == 200:
                    data = response.json()
                else:
                    print "API fetch error"
                    return False



    def printMovieList(self, movieList):
        for x in movieList:
            print "Movie: " + x.getName() + "\n Genre: " + ', '.join(
                x.getGenres()) + "\n  Release Date: " + x.getDate() + "\n"

    def printGenres(self):
        print "Total Genres: " + str(len(self.genresT)) + ""
        print "Genres: " + ', '.join(self.genresT)

