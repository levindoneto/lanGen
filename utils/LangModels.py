import nltk
from math import log2

''' Function for creating n-grams.
    @Parameters: List: sequenceuence, Integer: n (type of the n-gram).
    @Return: List of n-grams.
'''
def generateNGrams(sequence, n):
    ngrams = []
    for i in range(len(sequence)-n+1):
        ngrams.append(sequence[i:i+n])
    return ngrams

''' Function for counting how often each item occurs in a sequence.
    @Parameters: Tuple: N-Grams, Integer: n (type of the n-gram).
    @Return: Dictionary: token:frequency.
'''
def getNGramFrequencies(ngrams):
    frequencies = {}
    for token in ngrams:
        if (token in frequencies):
            newFrequency = str(int(frequencies[token]) + 1)
            frequencies.update({token: newFrequency})
        else: # Just in the first time a token is found
            frequencies.update({token: '1'})
    return frequencies

''' Function for adding an occurance of a gram considering the one which is
    following it.
    probabilities: {
        word_0: {
            next_0: occurance_0, ...
            next_n: occurance_n
        }, ...
        word_n: {
            next_0: occurance_0, ...
            next_n: occurance_n
        },
    }
    @Parameters: String: currentWord, nextWord
                 Dictionary: occurances.
    @Return: Dictionary: new occurances.
'''
def addOccurance(currentWord, nextWord, occurances):
    occurs = occurances
    if (currentWord in occurs):
        if (nextWord in occurs[currentWord]):
            aux = int(occurs[currentWord][nextWord])
            aux += 1
            occurs[currentWord][nextWord] = str(aux)
        else:
            occurs[currentWord].update({nextWord : "1"})
    else:
        occurs[currentWord] = {nextWord : "1"}
    return occurs

''' Function for getting occurances of n-grams (word by the previous one).
    @Parameters: Tuple: N-Grams.
    @Return: Dictionary: occurances.
'''
def getNGramOccurances(ngrams):
    occurs = {}
    currentWord = 0
    nextWord = 1
    for i in range(len(ngrams) - 1):
        occurs = addOccurance(ngrams[currentWord], ngrams[nextWord], occurs)
        currentWord += 1
        nextWord += 1
    return occurs
