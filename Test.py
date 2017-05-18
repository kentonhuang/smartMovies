import HashTable as h

import Comparison as comp
import LearningElement
import user_input
import fetcher

user = user_input.NewUser()
moviesInThreates = user.get_movies_threates()
Hash = h.HT([]) 
foundMovie = False

while foundMovie == False:
    user.runCount = user.runCount+1
    print ""
    print "-------------------------------------------"
    print "Run:", user.runCount, " Performance Measure:", user.performanceMeasure

    
     
    user_movie_genre = user.get_genre(Hash)
    if user_movie_genre!= False:
        Hash.updateProbs(user_movie_genre) 
    
        #Input moviesInTheater list, and Hash Table with genres returns a Movie Object
        movie = comp.returnMovie(moviesInThreates, Hash)
        for key, value in movie.iteritems():
            #Gets movie's prob
            #The run count has to be over 6 for the db to be properly primed
            print movie[key][1]
            if user.runCount > 6:
                if movie[key][1] == True:                
                    foundMovie = True
                    print "      Recommended Movie:", key.getName()
                    
    if user.performanceMeasure < -10 or  user.runCount > 15:
        foundMovie = True
        print "There are no recommended movies for you in Theaters"
