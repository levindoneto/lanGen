import random
import sys
from ast import literal_eval as make_tuple
from management import FileManagement
from utils import Formatting
from utils import System
import msvcrt # for key events

ESC = 27
ENTER = 13
ALT = 18

'''
Function for obtaining the first gram for starting a sentence.
@Parameter: Tuple: all the n-grams.
@Return: Tuple: first gram to start a phrase.
'''
def getFirstGram(ngrams):
    gram = input("\n> ")
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
    context = ()
    prob = 0 # initial probability of a context
    sentence = ''
    firstGram = getFirstGram(ngrams)
    sentence += Formatting.formatGram(firstGram[0]) + ' '
    sys.stdout.write(" " + Formatting.formatGram(firstGram[0]))
    context += firstGram
    prob += float(probabilities[firstGram][max(probabilities[firstGram])])
    i = ''
    maxGram = max(probabilities[firstGram])
    sentence += Formatting.formatGram(maxGram) + ' '
    context += maxGram
    prob *= float(probabilities[maxGram][max(probabilities[maxGram])])
    sys.stdout.flush()
    sys.stdout.write(" " + Formatting.formatGram(maxGram))
    while (True):
        if msvcrt.kbhit():
            key = ord(System.getKey())
            if (key == ENTER):
                sys.stdout.flush()
                if (Formatting.formatGram(maxGram) != max(probabilities[maxGram])[-1]):
                    maxGram = max(probabilities[maxGram])
                else:
                    maxGram = random.choice(ngrams)
                context += maxGram
                prob *= float(probabilities[maxGram][max(probabilities[maxGram])])
                sentence += Formatting.formatGram(maxGram[-1]) + ' '
                sys.stdout.write(" " + Formatting.formatGram(maxGram[-1]))
            elif (key == ESC):  # escape key
                print("\n\nFormatted sentence: ", Formatting.formatSentence(sentence))
                context = ()
                prob = 0
                manager(ngrams, probabilities)
            elif (key == ALT):
                FileManagement.saveContext(filename, context, str(prob))
