from utils import LangModels
from management import FileManagement
from management import SentenceGenerationManagement
import random
import pickle

NGRAM = 0
INFILE = 1
OUTFILE = 2

'''
Function that manages the generation of words for creation of sentences.
@Parameter: Dictionary: probabilities.
            Tuple: first gram to start a phrase.
@Return: Void.
'''
def managerSentences(probabilities, ngrams):
    print("Start with: ", SentenceGeneration.getFirstGram(ngrams))

'''
Function that manages the creation of directories and files.
@Parameter: Integer: cardinality of the requested n-grams' analysis.
            String: input file's path, output file's path.
@Return: Tuple: generated n-Grams.
'''
def manager(corpus, opts):
    nProb = opts[NGRAM]
    pathIn = opts[INFILE]
    pathOut = opts[OUTFILE]
    ngrams = LangModels.generateNGrams(corpus, nProb)
    firstGram = random.choice(ngrams)
    frequencies = LangModels.getNGramFrequencies(ngrams)
    occurs = LangModels.getNGramOccurances(ngrams)
    if (pathIn == ""): # The user has not loaded a pickle file with the probabilities
        probs = LangModels.getNGramProbabilities(occurs)
        if (pathOut != ""): # The user wants to save the pickle file with the probabilities
            FileManagement.savePickleFile(pathOut, probs)
    else:
        probs = FileManagement.loadPickleData(pathIn)
    return ngrams, probs
