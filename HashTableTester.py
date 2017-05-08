import HashTable as h
import Comparison as comp
import fetcher as f

fet = f.Fetcher()
moviesInThreates = []
fet.fetch(moviesInThreates, 15, 'theater')

L = ["Action", "Drama", "Comedy"] #create List of genres as strings 
Hash = h.HT(L) #create KB
print Hash.Hello() # check if Genres added to hash table
Hash.updateProbs(L) # update probabilties -- testing function 
R = ["Action", "Family", "Adventure"] # add new genre using update function
Hash.updateProbs(R) # call update function 
print Hash.getProbability("Action") # Test getProbabilty function
print Hash.Hello() # check results

#Input moviesInTheater list, and Hash Table with genres returns a Movie Object
movie = comp.returnMovie(moviesInThreates, Hash)
for key, value in movie.iteritems():
    #How to get movie info
    print key.getName()
    print key.getDate()
    print key.getGenres()
    #Gets movie's prob
    print movie[key][0]
    #Gets movie's true/false above/below threshold boolean
    print movie[key][1]