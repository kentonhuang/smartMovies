import HashTable as h
import fetcher as f

L = ["Action", "Drama", "Comedy"] #create List of genres as strings 
Hash = h.HT(L) #create KB
print Hash.Hello() # check if Genres added to hash table 
Hash.updateProbs(L) # update probabilties -- testing function 
R = ["Action", "Family"] # add new genre using update function 
Hash.updateProbs(R) # call update function 
print Hash.getProbability("Action") # Test getProbabilty function 
print Hash.Hello() # check results 
print Hash.topGenre() # top genre returned 
print Hash.secondTopGenre()


smartMovies = []
fet = f.Fetcher()
fet.smartFetch(Hash, smartMovies, 3)
fet.printMovieList(smartMovies)

fet.smartFetch(Hash, smartMovies, 5)
fet.printMovieList(smartMovies)

