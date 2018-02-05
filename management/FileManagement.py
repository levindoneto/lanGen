''' Function for getting parts of a text which are separeted with a space.
    @Parameters: String: path of the file.
    @Return: Tuple: fragments of the text.
'''
def getTextFragments(path):
    text = []
    with open(path) as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            line = line.lower()
            text.extend(line.split())
    return tuple(text) # Tuple with each element being a fragment from the text
