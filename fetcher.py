# Fetcher Class
# Author: Wai Myint


import requests
import apikey as api
import movie

class Fetcher:
    count = 0

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
                        genres.append((b for b in api.genre if b['id'] == y).next()['name'])
                    date = data['results'][self.count]['release_date']
                    m = movie.Movie(name, genres, date)
                    movieList.append(m)
                    self.count += 1
        else:
            return False

    def printMovieList(self, movieList):
        for x in movieList:
            print()


movieList = []
f = Fetcher()
f.fetch(movieList, 3)
f.fetch(movieList, 10)

for x in movieList:
    print "Movie: " +x.getName()+ "\n Genre: " + ' '.join(x.getGenres())+ "\n  Release Date: " +x.getDate()+ "\n"