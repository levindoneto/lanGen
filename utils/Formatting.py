import re

''' Function for Formatting n-grams.
    @Parameters: Tuple: n-gram to be formatted.
    @Return: String: formatted gram.
'''
def formatGram(ngram):
    return re.sub("[(',)]", '', str(ngram))

''' Function for Formatting sentences.
    @Parameters: Sentence: unformatted sentence.
    @Return: String: formatted sentence.
'''
def formatSentence(sentence):
    sentence = list(sentence)
    sentence[0] = sentence[0].upper()
    sentence = "".join(sentence)
    return sentence + '.\n'
