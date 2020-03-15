#This is a comment
#Comments help you to understand my code

#Program to print all permutations of a word

#word ----> Stores a word
#permutation ----> Stores all the permutations of the word


#Import permutations from itertools
from itertools import permutations


#Function to permutate a word
def permutate(word):

    #Stores all the permutations of the word as lists in a list
    permutation = list(permutations(word))

    #Stores permutations of the word as strings in a list
    permutation = [''.join(permutation) for permutation in permutation]

    #Prints all the permutations of the word as strings in a list
    print(permutation)
    
#Main function
def main():
    
    #Ask word input from user
    word = input('Please enter the word: ')

    #Print an empty line
    print()

    #Permutate the word
    permutate(word)
    
#If program is started as main process
#instead of being imported
if __name__ == '__main__':

    #Execute the main function
    main()
