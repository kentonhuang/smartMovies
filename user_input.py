"""Create a new user for movie recommendation AI

The class hierarchies are as follows:

NewUser ##A new user class
    get_genre ##Gets user input and sees if input(s) are valid movie genre
"""

import difflib
import fetcher

class NewUser:
    #List of movie genres as stated on IMBD
    #List of user choosen genre that will be returned
   
    performanceMeasure = 5;
    users_movie_genre_valid = []
    movieList = []
    moviePresented = [];
    f = fetcher.Fetcher()
    moviesInThreates = []
    f.fetch(moviesInThreates, 15, 'theater')
    
    def get_movies(self):
        print "Select Which Movie You Like, Type N for None"
        self.f.printMovieList()
        
    def get_genre(self):
        #Prints welcome message and shows user list of valid genres
        
        self.f.fetch(self.movieList, 5, 'popular')
        print "Do you like any of these movies? "
        count = 0
        for x in self.movieList: 
            if(x not in self.moviesInThreates):
                print count, x.getName()
                count = count + 1
        print ""
        print("Please enter in comma separated list.")
    
        #Get user input, valid input is in a comma separated list
        users_movie_genre_str = raw_input(">")

        #Convert user input to list form
        list_of_movies_liked = users_movie_genre_str.split(",")
        
        if(len(list_of_movies_liked) > 2):
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
     
            
    def get_movie_list(self):
        return self.movieList 
#______________________________________________________________________________

#user = NewUser()
#print user.get_genre()
_docex = """
user = NewUser()
user.get_genre()
"""
