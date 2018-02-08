import random
import sys
from ast import literal_eval as make_tuple

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
        return make_tuple("('" + gram + "',)")

'''
Function that manages the creation of words/sentences and manipulation of the
new contexts.
@Parameter: Tuple: n-grams, Dictionary: probabilities.
@Return: Void.
'''
def manager(ngrams, probabilities):
    sentence = ''
    firstGram = getFirstGram(ngrams)
    print(firstGram)
    sentence += str(firstGram)
    i = ''
    maxGram = max(probabilities[firstGram])
    sentence += str(maxGram)
    sys.stdout.write(str(maxGram))
    while (i != 's' and i == ''):
        i = input()
        maxGram = max(probabilities[maxGram])
        sentence += str(maxGram)
        sys.stdout.write(str(maxGram))
    print("\n\nSentence: ", sentence)
    # format next gram
    # save context
    # again...
    #TODO
