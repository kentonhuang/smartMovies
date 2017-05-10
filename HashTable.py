
# the hash table class 
class HashTable:
    def __init__(self):
        self.size = 30
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
        sum = 0
        for char in range(len(key)):
            sum = sum + ord(key[char])
        return sum%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)
# the main class         
class HT:
    # creates the KB
    # Param: list of strings 
    def __init__(self, genres):
        self.genres = genres
        self.probs=HashTable()
        for gen in self.genres:
            self.probs[gen] = 0.1
    #tetser function to print out Hashtable conetents 
    def Hello(self):
        print self.probs.slots
        print self.probs.data
    #update the probabilties in the KB 
    #param: list of strings 
    def updateProbs(self, glist):
        for gen in glist:
            
            if (self.probs[gen] is None):
                self.probs[gen] = 0.1
                self.genres.append(gen)
            else:
                self.probs[gen] = self.probs[gen] + 0.1
    #normalize function
    #return float
    def normalizeProbs(self):
        probToNorm = []
        for gen in self.genres:
            if self.probs[gen] is not None:
                probToNorm.append(self.probs[gen])
        prob_factor = 1 / sum(probToNorm)
        return prob_factor
    #get probabilty of a genre 
    #param: genre as a string 
    #return: float number 
    def getProbability(self,genre):
        num = self.normalizeProbs()
        return self.probs[genre]*num
        
    def topGenre(self):
        genName = self.genres[0]
        genMax = self.probs[self.genres[0]]
        for gen in self.genres:
            if (self.probs[gen] > genMax):
                genName = gen
                genMax = self.probs[gen]
        return genName 
                