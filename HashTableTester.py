import HashTable as h
L = ["Action", "Drama", "Comedy"] #create List of genres as strings 
Hash = h.HT(L) #create KB
print Hash.Hello() # check if Genres added to hash table 
Hash.updateProbs(L) # update probabilties -- testing function 
R = ["Action", "Family"] # add new genre using update function 
Hash.updateProbs(R) # call update function 
print Hash.getProbability("Action") # Test getProbabilty function 
print Hash.Hello() # check results 
