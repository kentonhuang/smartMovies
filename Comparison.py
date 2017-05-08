


#theater movies is a list of theater movies
#genreProbabilities is a Hash table of the genres from popular movies
def returnMovie(theaterMovies, genreProbabilities):
    genresinmovie = []
    for movie in theaterMovies:
        genresinmovie.append(movie.getGenres())

    Hash = genreProbabilities
    #Test if it is the correct Type
    #print(Hash.genres)
    #print(Hash.getProbability('Drama'))

    movieProbability = []
    for i in genresinmovie:
        total = 0.0
        for j in i:
                if(j in Hash.genres):
                    total = total + Hash.getProbability(j)
                    #if(key in genreProbabilities.keys()):
                     #   total = total + genreProbabilities[key]
        movieProbability.append(total)

    #print(movieProbability)
    #print(genresinmovie)

    movieProbabilityNormalized = normalizeMovieGenres(movieProbability)
    #print(movieProbabilityNormalized)
    moviesAndProbabilities = zip(theaterMovies, movieProbabilityNormalized)
    #print(moviesAndProbabilities)

    #Threshold (What should this number be?)
    threshold = 0.3
    topmovieProb = 0

    for movie, probability in moviesAndProbabilities:
        if probability > topmovieProb:
            topmovieProb = probability
            bestMovie = movie

    #True if above Threshold, false if below
    if (topmovieProb > threshold):
        return {bestMovie: (topmovieProb,True)}
    else:
        return {bestMovie: (topmovieProb,False)}


def normalizeMovieGenres(movielist):
    total = 0;
    for probability in movielist:
        total += probability

    #print total

    for i, val in enumerate(movielist):
        movielist[i] = val / total

    #CHECKS IF NORMALIZING CORRECTLY
    # normalize = 0
    #for normtotal in movielist:
    #    normalize += normtotal
    #print normalize

    return movielist