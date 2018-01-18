''' Function for creating n-grams
    @Parameters: List: Sequence, Integer: n (type of the n-gram)
    @Return: List of n-grams
'''
def generateNGrams(seq, n):
    ngrams = []
    for i in range(len(seq)-n+1):
        ngrams.append(seq[i:i+n])
    return ngrams

def test():
    return 5
