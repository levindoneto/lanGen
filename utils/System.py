import msvcrt # for key events

''' Function for getting a single char (key).
    @Parameters: Void.
    @Return: Char: pressed key.
'''
def getKey():
    char = msvcrt.getch()
    if char in b'\x00\xe0':
        char = msvcrt.getch()
    return char
