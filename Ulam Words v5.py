from time import time
from shutil import copyfile
import os.path

def int_to_string(word_length,n):
    """
    Inputs:
        word_length - int; length of intended word
        n - int; corresponds to a word of length word_length corresponding to n when read in binary
    Output: word of length word_length corresponding to n
    """

    base_str = bin(n)[2:]

    return base_str.zfill(word_length)

def is_ulam(word, ulam_words):
    """
    Inputs:
        word - string; word that needs to be tested
        ulam_words - dictionary of all Ulam words, indexed by length

    Output:
        true iff word is an Ulam word
    """

    word_length = len(word)

    num_reps = 0

    for l in range(1,word_length):
        #Split word into two subwords
        sub_word1 = word[0:l]
        sub_word2 = word[l:word_length]

        #Check that this isn't the same word twice
        if sub_word1 != sub_word2:
            #Convert subwords into integers
            sub_word1 = int(sub_word1, 2)
            sub_word2 = int(sub_word2, 2)

            if (sub_word1 in ulam_words[l]) and (sub_word2 in ulam_words[word_length - l]):
                num_reps += 1

                if num_reps > 1:
                    return False

    if num_reps == 0:
        return False

    return True

def read_Ulam_line(file):
    """
    Inputs:
        file - file in which Ulam words are stored.

    Outputs:
        length_info - boolean: true if the line begins with "Length"
        int_info - int; length of words if length_info = True; -1 if there are no remaining lines in file; the integer representing the Ulam word otherwise.
    """

    line = file.readline()

    #Check if there are any lines left in the file
    if not line:
        return False, -1

    #Check if this is a line describing lengths of words
    if line[0] == "L":
        length_info = True
        int_info = eval(line[7:])
    else:
        length_info = False
        int_info = eval(line)

    return length_info, int_info
    

def initialize_ulam(filename):
    """Initialize basic building blocks, using the given filename."""

    #Open the desired file
    file = open(filename,"r")

    #Create dictionary in which to store information
    ulam_words = {}

    length_info, int_info = read_Ulam_line(file)

    #Read through all lines in the file
    while(int_info != -1):
        #Check whether this line is telling us about word lengths
        if length_info:
            #If we are starting a new word length, store it and create a new empty set
            word_length = int_info
            ulam_words[word_length] = set([])
        else:
            #Otherwise, add new integer to the set
            ulam_words[word_length].add(int_info)

        length_info, int_info = read_Ulam_line(file)

    longest_word = word_length
    file.close()

    return ulam_words, longest_word


def next_Ulam_words(filename):
    """Calculates Ulam words of the next word length, starting from the given file."""

    #Initialize the data dictionary
    ulam_words, longest_word = initialize_ulam(filename)

    start_time = time()
    word_length = longest_word + 1

    #Set up file in which to append new Ulam words
    basename = "~/UlamWords_{}.txt".format(word_length)
    fullname = os.path.expanduser(basename)
    copyfile(filename,fullname)
    ulam_file = open(fullname,mode='a')

    ulam_file.write("Length " + str(word_length))
    ulam_file.write("\n")

    #Go through all words, represented as integers
    for n in range(2**word_length):
        #Convert the integer to a word
        word = int_to_string(word_length,n)

        #Test if the word is Ulam and add the corresponding integer to the file if it is
        if is_ulam(word, ulam_words):
            ulam_file.write(str(n))
            ulam_file.write("\n")

    end_time = time()
    ulam_file.close()

    return end_time - start_time
