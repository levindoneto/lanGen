''' Function for creating n-grams
    @Parameters: List: sequenceuence, Integer: n (type of the n-gram)
    @Return: List of n-grams
'''
def generateNGrams(sequence, n):
    ngrams = []
    for i in range(len(sequence)-n+1):
        ngrams.append(sequence[i:i+n])
    return ngrams

''' Function for counting how often each item occurs in a sequenceuence
    @Parameters: Tuple: N-Grams, Integer: n (type of the n-gram)
    @Return: Dictionary: token:frequency
'''
def getNGramFrequencies(ngrams):
    frequencies = {}
    for token in ngrams:
        if (token in frequencies):
            newFrequency = str(int(frequencies[token]) + 1)
            frequencies.update({token: newFrequency})
        else:
            frequencies.update({token: '0'})
    return frequencies
