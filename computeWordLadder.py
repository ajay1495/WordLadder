import string
import copy

# Alters the letter at index to toLetter 
def alterOneLetterTo(stringToAlter, index, toLetter):
    s = list(stringToAlter)
    s[index] = toLetter
    return "".join(s)

# Breadth first search to find optimal word ladder from startingWord to endWord 
def computeWordLadderBreadthFirst(startingWord, endWord, dictionary):
    # paths is a list of wordladders
    paths = [[startingWord.lower()]]
    endWord = endWord.lower()
    
    # Breadth first search to find the best word ladder 
    while len(paths) > 0:
        curWordLadder = paths.pop(0)
        curLastWord = curWordLadder[-1]

        # Compute all possible alterings of the current last word 
        possibleNextStrings = []

        # Replace letters
        for ii in range(len(curLastWord)):
            for letter in list(string.ascii_lowercase):
                newWord = alterOneLetterTo(curLastWord, ii, letter)
                possibleNextStrings.append(newWord)
                    
        # Can also swap characters 
        for ii in range(len(curLastWord)):
            for jj in range(ii, len(curLastWord)):
                letterIIToSwap = curLastWord[ii]
                
                newWord = alterOneLetterTo(curLastWord, ii, curLastWord[jj])
                newWord = alterOneLetterTo(newWord, jj, letterIIToSwap)
                
                possibleNextStrings.append(newWord)
        
        # Can also add the add/remove characters functionality here, if desired
        # Ex. add letter
        #for ii in range(len(curLastWord)):
        #    for letter in list(string.ascii_lowercase):
        #        newWord =  curLastWord[:ii] + letter + curLastWord[ii:]
        #        possibleNextStrings.append(newWord)        
        
        # Ex. remove letter
        #for ii in range(len(curLastWord)):
        #    newWord =  curLastWord[:ii] + curLastWord[ii+1:]
        #    possibleNextStrings.append(newWord)   
        
        # Now add all possibilities to the end of paths list, if string is valid 
        for possNextStr in possibleNextStrings:
            if possNextStr in dictionary and possNextStr not in curWordLadder:
                possWordLadder = copy.deepcopy(curWordLadder)
                possWordLadder.append(possNextStr)

                paths.append(possWordLadder)

                if possNextStr == endWord:
                    return possWordLadder

            
dictionaryFile = open("dictionary.txt")
dictionary = set()

for word in dictionaryFile: 
    dictionary.add(word.rstrip('\n')) 

print "Dictionary read!"

print computeWordLadderBreadthFirst("code", "data", dictionary)
    