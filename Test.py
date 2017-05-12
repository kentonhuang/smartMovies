import HashTable as h

import Comparison as comp
import LearningElement
import user_input
import fetcher

user = user_input.NewUser()
moviesInThreates = user.get_movies_threates()
Hash = h.HT([]) 
foundMovie = False
runCount = 0
while foundMovie == False:
    runCount = runCount+1
    print ""
    print "-------------------------------------------"
    print "Run:", runCount, " Performance Measure:", user.performanceMeasure
    user_movie_genre = user.get_genre(Hash)
    if user_movie_genre!= False:
        Hash.updateProbs(user_movie_genre) 
    
        #Input moviesInTheater list, and Hash Table with genres returns a Movie Object
        movie = comp.returnMovie(moviesInThreates, Hash)
        for key, value in movie.iteritems():
        #How to get movie info
            print "      Name:", key.getName()
            print "      Date:", key.getDate()
            print "      Genres:", key.getGenres()
            #Gets movie's prob
            print "      Prob:", movie[key][0]
            #Gets movie's true/false above/below threshold boolean
            print "      Recommended:",movie[key][1]

