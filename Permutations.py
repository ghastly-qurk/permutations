#This is a comment
#Comments help you to understand my code

#Program to print all permutations of a word
#except the word itself

#word ----> Stores a word
#permutation ----> Stores all the permutations of the word


#Import permutations from itertools
from itertools import permutations

#Function to permutate a word
def permutate(word):

    #Print an empty line
    print('')

    #Stores all the permutations of the word as a list
    permutation = list(permutations(word))

    #Loop untill all permutations are printed
    for permutation in permutation:
        
        #If permutation is not the word itself
        if ''.join(permutation) != word:
            
            #Print permutation as a string
            print(''.join(permutation))

#Main function
def main():
    
    #Ask word input from user
    word = input('Please enter the word: ')

    #Permutate the word
    permutate(word)
    
#If program is started as main process
#instead of being imported
if __name__ == '__main__':

    #Execute the main function
    main()
