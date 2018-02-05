''' Function for creating n-grams.
    @Parameters: List: sequenceuence, Integer: n (type of the n-gram).
    @Return: List of n-grams.
'''
def generateNGrams(sequence, n):
    ngrams = []
    for i in range(len(sequence)-n+1):
        ngrams.append(sequence[i:i+n])
    return ngrams

''' Function for counting how often each item occurs in a sequence.
    @Parameters: Tuple: N-Grams, Integer: n (type of the n-gram).
    @Return: Dictionary: token:frequency.
'''
def getNGramFrequencies(ngrams):
    frequencies = {}
    for token in ngrams:
        if (token in frequencies):
            newFrequency = str(int(frequencies[token]) + 1)
            frequencies.update({token: newFrequency})
        else: # Just in the first time a token is found
            frequencies.update({token: '1'})
    return frequencies

''' Function for getting probabilities of n-grams.
    @Parameters: Tuple: N-Grams, Dictionary: frequencies.
    @Return: Dictionary: probabilities.
'''
def getNGramProbabilities(ngrams, frequencies):
    print("Im here")
    probabilities = [cgram/freq for cgram, freq in zip(ngrams, frequencies)]
    #ngram_prob = sum(math.log(prob, 10) for prob in probabilities)
