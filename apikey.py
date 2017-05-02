# API call to themoviedb.org

import requests


"""Variables"""
"""API Base: https://developers.themoviedb.org/3/"""

v3 = '?api_key=869b54a272f385c15528cc1742110c86';
base = 'https://api.themoviedb.org/3/'
end = '&language=en-US&page=1'

response = requests.get(base + "genre/movie/list" + v3 + end)
data = response.json()
genre = data['genres']

#print((item for item in genre if item['id'] == 28).next()['name'])





#print(data['results'][2]['title'])

