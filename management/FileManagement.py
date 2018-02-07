import pickle

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

''' Function for putting a dictionary in a pickle file.
    @Parameters: String: name of the file (without the format),
                 Dictionary: data structure to be stored.
    @Return: Void.
'''
def savePickleFile(fileName, dictionary):
    with open(fileName + ".pickle", "wb") as fp:
        pickle.dump(dictionary, fp, protocol = pickle.HIGHEST_PROTOCOL)

''' Function for loading a pickle file into a dictionary.
    @Parameters: String: path of the file.
    @Return: Dictionary: loaded cata structure.
'''
def loadPickleData(filePath, dictionary):
    with open(filePath, "rb") as fb:
        return pickle.load(fb)
