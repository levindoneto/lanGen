'''
Usage:
  lm (-n INT [-s <path>]|-l <path>)

Options:
  -n INT                          The n used to get n-gram probabilities
  -s <path>, --save_model <path>  The path to save the model to
  -l <path>, --load_model <path>  The path to load the model from


After generating the model/ loading it from a pickle file this program
provides an interactive shell.
Here either just enter can be pressed in order to generate a sentence or
a prefix can be inserted for being used as seed to generate only sentences
that start with the given prefix.
'''
import docopt
import LangModels
import FileManagement
import nltk
from nltk.collocations import *

# nltk.download('punkt')

INPUT_TEXT = 'smallText.txt';

def main(opts):
    raise NotImplementedError


if __name__ == '__main__':
    #opts = docopt.docopt(__doc__)
    #print(opts)
    shakespeareCorpus = FileManagement.getTextFragments(INPUT_TEXT)

    unigrams = LangModels.generateNGrams(shakespeareCorpus, 1)
    bigrams = LangModels.generateNGrams(shakespeareCorpus, 2)
    trigrams = LangModels.generateNGrams(shakespeareCorpus, 3)
    quadrigrams = LangModels.generateNGrams(shakespeareCorpus, 4)

    unigramFreq = LangModels.getNGramFrequencies(unigrams)
    bigramsFreq = LangModels.getNGramFrequencies(bigrams)
    trigramsFreq = LangModels.getNGramFrequencies(trigrams)
    quadrigramsFreq = LangModels.getNGramFrequencies(quadrigrams)
    # Tests - N-Grams' Generation

    print('Unigrams:\n', unigrams, '\n\n')
    '''
    print('Bigrams:\n', bigrams, '\n\n')
    print('Trigrams:\n', trigrams, '\n\n')
    print('Quadrigrams:\n', quadrigrams, '\n\n')
    '''
    # Tests - Tokens' Frequencies

    print('Unigrams Frequencies:\n', unigramFreq, '\n\n')
    '''
    print('Bigrams Frequencies:\n', bigramsFreq, '\n\n')
    print('Trigrams Frequencies:\n', trigramsFreq, '\n\n')
    print('Quadrigrams Frequencies:\n', quadrigramsFreq, '\n\n')
    '''
    #main(opts)

    f = open('smallText.txt')
    raw = f.read()

    tokens = nltk.word_tokenize(raw)

    #Create your bigrams
    bgs = nltk.ngrams(tokens, n=1)

    #compute frequency distribution for all the bigrams in the text
    fdist = nltk.FreqDist(bgs)
    for k,v in fdist.items():
        print (k,v)
