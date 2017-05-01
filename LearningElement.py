#Learning Element Class
#Author: Soneer Sainion
#Example:
# le1 = LearningElement(5)   |||||perforamce measure of 5, gives 5 movies before score can become negative
#le1.parseUserResponse("Tarzan", False)    ||||| We presented user with Tarzan, user did no like it. WIll update PM and Jorges Prob. Run 6 times

class LearningElement:
    
    def __init__(self, performance_measure):
      self.performance_measure = performance_measure

    
    def parseUserResponse(self, Movie, liked):
        if liked == True:
            #Soneer's function
            self.incrementPerformanceMeasure()
            #add movie to list of liked movies and remove from movie's list
            #---------------------------------------------
            #Jorge's function
            #JorgesClass.incrementGenres(Movie.getGenres())
            #JorgesClass.incrementDate(Movie.getDate())
            #----------------------------------------------
            #Kenton's part
            #Agent is doing good, present user with new movie
            pass
        else:
            #Soneer's function
            self.decrementPerformanceMeasure()
            #add movie to list of disliked movies and remove from movie's list
            #---------------------------------------------
            #Jorge's method
            #JorgesClass.decrementGenres(Movie.getGenres())
            #JorgesClass.decrementDate(Movie.getDate())
            pass
        print self.performance_measure
    def incrementPerformanceMeasure(self):
        self.performance_measure += 1 
        
    def decrementPerformanceMeasure(self):
        self.performance_measure -= 1 
        #If Performance Measure drops to low use a Problem Generator
        if self.performance_measure < 0:
            self.problemGenerator()
    
      
    #Decides whether to use  reQueryUser,reWeightGenres or pullMoreMovies to increase PM 
    def problemGenerator(self):
        #if blah then use reQueryUser
        #else if blah then use reWeightGenres
        #else if no more movies or PM drops too low use pullMoreMovies
        #Let Kentons Part present user with movie after we try to fix our problem
        print "Using Problem Generator, will either update Jorge's Prob. or worse case tell Wai to get more movies"
        pass 
                  
    #If user genres weight becomes to low, ask if they are still interested
    def reQueryUser(self, UserInput):
        pass
            
    #If one genre is no longer beign liked, change genres weight
    def reWeightGenres(self, JorgesPC):
        pass   
               
    #Slowest & Worst fix for low PM. Use in worst case 
    def pullMoreMovies(self, WaisPart):
        pass