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
   
    
    users_movie_genre_valid = []
    movieList = []
    f = fetcher.Fetcher()
    f.fetch(movieList, 10)
    
    def get_genre(self):
        #Prints welcome message and shows user list of valid genres
        print "*---------Welcome New User--------*"
        print ""
        print "What is your favorite movie genre?"
        print ', '.join(self.f.genresT)
        print ""
        print("Please enter in comma separated list.")
    
        #Get user input, valid input is in a comma separated list
        users_movie_genre_str = raw_input(">")

        #Convert user input to list form
        users_movie_genre_unvalid = users_movie_genre_str.split(",")
        
        #Loop through user input genres and checks if they are valid, looks for close matches for misspellings
        i = 0
        while i < len(users_movie_genre_unvalid):
            current_genre = users_movie_genre_unvalid[i].lstrip().lower().title()
            if current_genre in self.f.genresT and current_genre not in self.users_movie_genre_valid:
                #print "Valid Movie Genre:", current_genre
                self.users_movie_genre_valid.append(current_genre)
                #Adds Genre to list to be added to user KB
            else:
                #print "Invalid Movie Genre:", users_movie_genre_unvalid[i]
                close_matches = difflib.get_close_matches(users_movie_genre_unvalid[i],self.f.genresT)
                #print "Close Matches:",  close_matches
                j = 0
                while j < len(close_matches):      
                    if close_matches[j] not in self.users_movie_genre_valid:
                        self.users_movie_genre_valid.append(close_matches[j])
                    j += 1
                #Adds close match to list to be added to user KB
            i += 1
    
        #Checks if there are any valid genres, if not repeat method
        if not self.users_movie_genre_valid:
            print "Please input at least 1 category"    
            print "" 
            NewUser().get_genre()
        #Returns list of movie genres
        else:
            print "User Genre List"
            print self.users_movie_genre_valid
            return self.users_movie_genre_valid
            
    def get_movie_list(self):
        return self.movieList 
#______________________________________________________________________________

#user = NewUser()
#print user.get_genre()
_docex = """
user = NewUser()
user.get_genre()
"""
