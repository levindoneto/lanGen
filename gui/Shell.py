''' Function for showing the use and available options to the user.
    @Parameters: Void.
    @Return: Void.
'''
def menu():
    print(
        '''Usage:
          lm (-n INT [-s <path>]|-l <path>)

        Options:
          -n INT                          The n used to get n-gram probabilities
          -s <path>, --save_model <path>  The path to save the model to
          -l <path>, --load_model <path>  The path to load the model from
        '''
    )

    options = input("$ ")
