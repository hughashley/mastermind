

class NewGame:
    
    def __init__(self, guess, ref):
        self.guess = [num for num in guess] #extract int's from guess input string
        self.ref = [num for num in ref] #extract int's from reference input string
        self.__compare__(self.guess, self.ref) #compare initial pair

    def __guess__(self, guess): 
        ref = self.ref #define ref in newGuess
        guess = [num for num in guess] #extract int's from new guess
        self.__compare__ (guess, ref) #compare new guess against reference

    def __compare__(self, guess, ref):
        white = 0 #init white
        black = 0 #init black
        flag = False #init white flag
        for i in range(4): #loop from 0 n
            if ref[i]==guess[i]: #look for direct compare
                white+=1 #increment white
                flag = True #set white flag to true
                pass
            elif flag == False and guess[i]==ref[i-1]: #check for flag and 
                black+=1 #increment black
            else:
                flag = False #reset flag
        print(white, "white", black, "black") #print results of compare

    def __version__(self):
        print("0.9.0") #version



           


