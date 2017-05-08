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

movie = comp.returnMovie(moviesInThreates, Hash)
for key, value in movie.iteritems():
    print key.getName()
    print key.getDate()
    print key.getGenres()
    print movie[key][1]