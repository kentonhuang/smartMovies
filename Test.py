import imdb
import LearningElement
import user_input
import fetcher

user = user_input.NewUser()
user_movie_genre = user.get_genre()
imbd_movie_list = user.get_movie_list()
le1 = LearningElement.LearningElement(5,user_movie_genre, imbd_movie_list)



print "_________________________________________________________"
print "Current Performance Measure:", le1.performance_measure
print ""
#Kentons logic, wrote this just to do a simple test 
for x in imbd_movie_list:
    #print "Movie: " +x.getName()+ "\n Genre: " + ' '.join(x.getGenres())+ "\n  Release Date: " +x.getDate()+ "\n"
    for ug in user_movie_genre:
        if ug in ' '.join(x.getGenres()):
            print ""
            print "----------------"
            print x.getName()
            print "Like/Dislike"
            current_input =  raw_input(">")
            if current_input == "Like":
                le1.parseUserResponse(x, True) 
            if current_input == "Dislike":
                le1.parseUserResponse(x, False) 
                
  
#   #perforamce measure of 5, gives 5 movies before score can become negative
#le1.parseUserResponse("Tarzan", False)  
