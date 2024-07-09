
def freword(filepath):
    with open (filepath) as file:
        counts=dict()
        for line in file:
            words=line.split()
            for word in words:
                counts[word]=counts.get(word,0)+1

        maxcount=None
        maxword=None
        for word, count in counts.items():
            if maxcount is None or count > maxcount:
                maxword=word
                maxcount=count
    return (f"The most frequent word is :{maxword}, and the number of times is: {maxcount}")
freqword('iso.txt')


