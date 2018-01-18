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
