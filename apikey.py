# API call to themoviedb.org

import requests


"""Variables"""
"""API Base: https://developers.themoviedb.org/3/"""

v3 = '?api_key=869b54a272f385c15528cc1742110c86';
base = 'https://api.themoviedb.org/3/'
genre = 'genre/movie/list'
popular = 'movie/popular'
theater = 'movie/now_playing'
end = '&language=en-US&page='

response = requests.get(base + genre + v3 + end + '1')
data = response.json()
genre = data['genres']

#print((item for item in genre if item['id'] == 28).next()['name'])





#print(data['results'][2]['title'])

