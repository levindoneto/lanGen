NGRAM = 0
INFILE = 1
OUTFILE = 2

''' Function for getting and parsing the user's input.
    @Parameters: Void.
    @Return: List: [NGRAM] -> Integer
                   [INFILE] -> String
                   [OUTFILE] -> String
'''
def getListOptions():
    listOpts = []
    listOpts.append(0)
    listOpts.append('')
    listOpts.append('')
    options = input("$ ")
    options = options.split()
    if (options[0] != 'lm'):
        print("Invalid option\nIt shall be lm")
    else:
        if (options[1][0] == '(' and options[-1][-1] == ')'):
            if (options[1][1:] == "-n"):
                listOpts[NGRAM] = int(options[2])
                if(options[3] == "[-s"):
                    listOpts[INFILE] = options[4][0:-1]
                if(options[3] == "-l"): # no -s
                    listOpts[OUTFILE] = options[4][0:-1]
                if (len(options) > 5):
                    if(options[5] == "-l"):
                        listOpts[OUTFILE] = options[6][0:-1]
            else:
                print("The option -n must used before the number of n-grams")
        else:
            print("The options must be between parenthesis")
    return listOpts

''' Function for showing the use and available options to the user.
    @Parameters: Void.
    @Return: Void.
'''
def menu():
    print(
        '''                                                                                 |
        Usage:                                                                   |
          lm (-n INT [-s <path>]|-l <path>)                                      |
          Example:                                                               |
              lm (-n 1 [-s in.pickle] -l in.pickle)                              |
              -> Unigrams                                                        |
              -> Saving in the file in.pickle                                    |
              -> Loading the file in.pickle                                      |
                                                                                 |
        Options:                                                                 |
          -n INT                          The n used to get n-gram probabilities |
          -s <path>, --save_model <path>  The path to save the model to          |
          -l <path>, --load_model <path>  The path to load the model from        |
                                                                                 |
        Exit:                                                                    |
          [CTRL] + [c]                                                           |
_________________________________________________________________________________+
        '''
    )

def showSentencesInterface():
    print(
        '''
__________________________________________________________________________________
        Sentences Generator                                                      |
                                                                                 |
        Usage:                                                                   |
          - Enter with [ENTER] for starting with a random word                   |
          - Enter with a prefix/word for starting with a specific word           |
                                                                                 |
        Options:                                                                 |
          - [ENTER] for putting more words into the sentence                     |
          - [ESC] for stopping the generation and finish the sentence            |
          - [s] for saving the context into the loaded file                      |
                                                                                 |
        Exit:                                                                    |
          [CTRL] + [c]                                                           |
_________________________________________________________________________________+
    '''
    )
