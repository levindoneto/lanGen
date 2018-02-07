import random

'''
Function for obtaining the first gram for starting a sentence.
@Parameter: Tuple: all the n-grams.
@Return: Tuple: first gram to start a phrase.
'''
def getFirstGram(ngrams):
    gram = input()
    if (gram == ""):
        return random.choice(ngrams)

'''
Function that manages the creation of words/sentences and manipulation of the
new contexts.
@Parameter: Void.
@Return: Void.
'''
def manager(ngrams):
    firstGram = getFirstGram(ngrams)
    print("firstGram: ", firstGram)
    #TODO
