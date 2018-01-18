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

INPUT_TEXT = 'shakespeare.txt';

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

    # Tests - N-Grams' Generation
    print('Unigrams:\n', unigrams, '\n\n')
    print('Bigrams:\n', bigrams, '\n\n')
    print('Trigrams:\n', trigrams, '\n\n')
    print('Quadrigrams:\n', quadrigrams, '\n\n')

    #main(opts)
