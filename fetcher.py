# Fetcher Class
# Author: Wai Myint


import requests
import apikey as api
import movie



class Fetcher:
    theater = 0
    popular = 0
    smart = 0
    popular_page = 1
    theater_page = 1
    smart_page = 1
    genresT = []
    smart_genresT = []

    def __init__(self):
        pass

    def smartFetch(self, hashTable, movieList, a=1):
        if hashTable is None or movieList is None:
            print "Please pass a initiated hashtable or movieList"
            return False

        response = requests.get(api.base + api.popular + api.v3 + api.end + str(self.smart_page))
        ct = self.smart

        if response.status_code != 200:
            print "API fetch failed"
            return False

        data = response.json()
        top = hashTable.topGenre()
        second = hashTable.secondTopGenre()

        x = 0
        while x < a:
            if ct < len(data['results']):
                genres = []
                for y in data['results'][ct]['genre_ids']:  # get genre(s) of current movie
                    gName = (b for b in api.genre if b['id'] == y).next()['name']
                    genres.append(gName)
                if top in genres and second in genres:  # check if top & second genre is in the current movie Genre list
                    # movie has the top and second genre, complete gathering information
                    name = data['results'][ct]['original_title']
                    date = data['results'][ct]['release_date']
                    m = movie.Movie(name, genres, date)
                    movieList.append(m)  # add it to the movieList passed in the funct. arguments
                    if top not in self.smart_genresT:
                        self.smart_genresT.append(top)
                    if second not in self.smart_genresT:
                        self.smart_genresT.append(second)
                    x += 1
                self.smart += 1
                ct = self.smart
            else:
                if self.smart_page > data['total_pages']:
                    print "Cannot pull anymore movies.. ran out"
                    return False
                self.smart_page += 1
                self.smart = 0
                response = requests.get(api.base + api.popular + api.v3 + api.end + str(self.smart_page))
                ct = self.smart

                if response.status_code != 200:
                    print "API fetch failed"
                    return False

                data = response.json()

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
                # print " # of genres: " +str(len(self.genresT))
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
