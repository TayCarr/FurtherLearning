#frequency finder
#www.nostarch.com/crackingcodes

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getLetterCount(message):
    #returns a dict with keys of single letters and values of the count of how many times they appear in the message give
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1

    return letterCount

def getItemAtIndexZero(items):
    return items[0]

def getFrequencyOrder(message):
    #returns a string of the alphabet letters arranged in order of most frequent in message

    #get a dict of each letter and its freq count
    letterToFreq = getLetterCount(message)

    #make a dict of each freq count to letter with that freq
    freqToLetter = {}
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)

    #put each list of letters in reverse "ETAOIN" order, then convert to string
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    #convert freqtoletter dict to a list of tuple (key, value) then sort
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)

    #letters ordered by freq, extract all letters for final str
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)

def englishFreqMatchScore(message):
    #return the number of matches that the string in the message param has when its letter freq is compared to english
    #a match is how many of its six most frequent and six least frequent letters are among the english versions
    freqOrder = getFrequencyOrder(message)

    matchScore = 0
    #find how many matches in 6 most common
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1
    #find uncommon match in 6 least
    for uncommonLetter in ETAOIN[-6:]:
        if uncommonLetter in freqOrder[-6:]:
            matchScore += 1

    return matchScore
