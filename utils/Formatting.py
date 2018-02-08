import re

''' Function for creating n-grams.
    @Parameters: Tuple: n-gram to be formatted.
    @Return: String: formatted n-grams.
'''
def formatNGram(ngram):
    return re.sub("[(',)]", '', str(ngram))
