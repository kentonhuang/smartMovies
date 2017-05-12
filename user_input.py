"""Create a new user for movie recommendation AI

The class hierarchies are as follows:

NewUser ##A new user class
    get_genre ##Gets user input and sees if input(s) are valid movie genre
"""

import difflib
import fetcher
import HashTable as h
class NewUser:
    #List of movie genres as stated on IMBD
    #List of user choosen genre that will be returned
   
    performanceMeasure = 2
    users_movie_genre_valid = []
    movieList = []
    moviePresented = [];
    f = fetcher.Fetcher()
    moviesInThreates = []
    f.fetch(moviesInThreates, 8, 'theater')
    f.printMovieList(moviesInThreates)
    Hash = h.HT([]) 
    def get_movies(self):
        print "Select Which Movie You Like, Type N for None"
        self.f.printMovieList()
        
    def get_genre(self, HashINC):
        #Prints welcome message and shows user list of valid genres
        self.Hash = HashINC
        if self.performanceMeasure < 0: 
            print "Smart Fetch" 
            self.f.smartFetch(self.Hash, self.movieList, 3) # Will add 3 movies that has the top 2 genres from the Hash table
        
        else:
            print "Normal Fetch"
            self.f.fetch(self.movieList, 3, 'popular')
        print "Do you like any of these movies? "
        count = 0
        for x in self.movieList: 
            if(x not in self.moviesInThreates):
                print "    ",count, x.getName()
                count = count + 1
        print ""
        print("    Please enter in comma separated list.")
    
        #Get user input, valid input is in a comma separated list
        correctFormat = False;
        while correctFormat == False:
            correctFormat = True
            users_movie_genre_str = raw_input("    >")
            if users_movie_genre_str == "":
                self.movieList = []     
                self.performanceMeasure = self.performanceMeasure - 1
                return False
            #Convert user input to list form
            list_of_movies_liked = users_movie_genre_str.split(",")
            for value in list_of_movies_liked:
                try:
                    w = int(value.lstrip())
                    if w < 0 and w <3:
                        correctFormat = False 
                except ValueError as verr:
                    correctFormat= False
                    print "    ",verr       
              
            if correctFormat == False:
                 print("    Please enter in comma separated list.")
                 print("    Example: ")
                 print("    >0,2")
    
        if(len(list_of_movies_liked) > 1):
            self.performanceMeasure = self.performanceMeasure + 1
        else:          
            self.performanceMeasure = self.performanceMeasure - 1
            #checkProblemGeneator TODO:
        
        #Loop through user input genres and checks if they are valid, looks for close matches for misspellings
        list_of_all_genres = []
        i = 0
        while i < len(list_of_movies_liked):
            #print self.movieList[int(list_of_movies_liked[i])].getName(), "  ,", self.movieList[int(list_of_movies_liked[i])].getGenres()
            for movie in self.movieList[int(list_of_movies_liked[i])].getGenres():
                 list_of_all_genres.append(movie)
            i += 1
        self.movieList = []
        return list_of_all_genres
     
    def get_movies_threates(self):
        return self.moviesInThreates 
        
    def get_movie_list(self):
        return self.movieList 
#______________________________________________________________________________

#user = NewUser()
#print user.get_genre()
_docex = """
user = NewUser()
user.get_genre()
"""
