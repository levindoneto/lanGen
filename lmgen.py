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

import sys
import docopt
import management.AppManagement as Management
import gui.Shell as Shell

def main(args):
    Shell.menu()
    #Management.manager(n, inFile, outFile)

if __name__ == '__main__':
    main(sys.argv)
