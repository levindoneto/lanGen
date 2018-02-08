'''
Usage:
  lm (-n INT [-s <path>]|-l <path>)

Options:
  -n INT                          The n used to get n-gram probabilities
  -s <path>, --save_model <path>  The path to save the model to
  -l <path>, --load_model <path>  The path to load the model from


After generating the model and loading it from a pickle file this program
provides an interactive shell.
Here either just enter can be pressed in order to generate a sentence or
a prefix can be inserted for being used as seed to generate only sentences
that start with the given prefix.
'''

import sys
import os
import docopt
import management.FileManagement as FileManagement
import management.AppManagement as AppManagement
import management.SentenceGenerationManagement as SentenceGenerationManagement
import gui.Shell as Shell

DEFAULT_CORPUS = "tests/shakespeare.txt"

def main(args):
    os.system("cls")
    try:
        pickleFile = args[1]
    except:
        pickleFile = DEFAULT_CORPUS
    fragments = FileManagement.getTextFragments(pickleFile)
    Shell.menu()
    while True:
        options = Shell.getListOptions()
        if (options != -1):
            ngrams, probs = AppManagement.manager(fragments, options)
            os.system("cls")
            options = Shell.showSentencesInterface()
            SentenceGenerationManagement.manager(ngrams, probs)
        else:
            main(args)

if __name__ == '__main__':
    main(sys.argv)
