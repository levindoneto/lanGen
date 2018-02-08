import random
import sys
from ast import literal_eval as make_tuple
from management import FileManagement
from utils import Formatting
from utils import System
import msvcrt # for key events

ESC = 27
ENTER = 13

'''
Function for obtaining the first gram for starting a sentence.
@Parameter: Tuple: all the n-grams.
@Return: Tuple: first gram to start a phrase.
'''
def getFirstGram(ngrams):
    gram = input("> ")
    if (gram == ""):
        return random.choice(ngrams)
    else:
        if (make_tuple("('" + gram + "',)") in ngrams):
            return make_tuple("('" + gram + "',)")
        else:
            return random.choice(ngrams)

'''
Function that manages the creation of words/sentences and manipulation of the
new contexts.
@Parameter: Tuple: n-grams, Dictionary: probabilities.
@Return: Void.
'''
def manager(ngrams, probabilities):
    sentence = ''
    firstGram = getFirstGram(ngrams)
    sentence += Formatting.formatNGram(firstGram) + ' '
    sys.stdout.write(" " + Formatting.formatNGram(firstGram))
    i = ''
    maxGram = max(probabilities[firstGram])
    sentence += Formatting.formatNGram(maxGram) + ' '
    sys.stdout.flush()
    sys.stdout.write(" " + Formatting.formatNGram(maxGram))
    while (True):
        if msvcrt.kbhit():
            key = ord(System.getKey())
            if (key == ENTER):  # ord('a')
                sys.stdout.flush()
                maxGram = max(probabilities[maxGram])
                sentence += Formatting.formatNGram(maxGram[-1]) + ' '
                sys.stdout.write(" " + Formatting.formatNGram(maxGram[-1]))
            elif (key == ESC):  # escape key
                break
    print("\n\nFormatted sentence: ", sentence)
    # save context
