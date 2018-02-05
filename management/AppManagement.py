from utils import LangModels
from management import FileManagement

'''
Function that manages the creation of directories and files.
@Parameter: Integer: cardinality of the requested n-grams' analysis.
            String: input file's path, output file's path.
@Return: Void, it only saves the model in the file specified by pathOut.
'''
def manager(corpus, nProb, pathIn, pathOut):
    ngrams = LangModels.generateNGrams(corpus, nProb)
    frequencies = LangModels.getNGramFrequencies(ngrams)
    probabilities = LangModels.getNGramProbabilities(ngrams, frequencies)
