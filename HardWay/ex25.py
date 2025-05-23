#exercise 25 Even More Practice 
'''
   more practice for functions and variables 
   instead wont be runnng this but will import it in a python shell 
   TO RUN IT in the terminal:
    >python3  
    >import ex25
    then you can type like sentence = "my sentence of words" then words = ex25.break_words(sentence)
    to quit out of python and youll go back to terminal
    >quit()
'''

def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes a full sentence and returns the words sorted"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of a sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last words of a sentence"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)