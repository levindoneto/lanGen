from utils import LangModels
from management import FileManagement
import random
import pickle

NGRAM = 0
INFILE = 1
OUTFILE = 2

'''
Function that manages the creation of directories and files.
@Parameter: Integer: cardinality of the requested n-grams' analysis.
            String: input file's path, output file's path.
@Return: Void, it only saves the model in the file specified by pathOut.
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
