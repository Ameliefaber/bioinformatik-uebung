def FasterFrequentWords (text,k):
    FrequencyArray = ComputingFrequencies(text,k)
    maxFrequency = max(FrequencyArray)
    FrequentPatterns = list()
    for i in range(len(FrequencyArray)):
        if FrequencyArray[i] == maxFrequency:
            pattern = NumberToPattern(i,k)
            FrequentPatterns.append (pattern)
    return FrequentPatterns
            

def NumberToPattern (index,k):
    pattern = ""
    for i in range(k):
        faktor = 4**(k-1-i)
        if faktor*3 <= index:
            pattern+="T"
            index-=faktor*3
        elif faktor*2 <= index:
            pattern+="G"
            index-=faktor*2
        elif faktor*1 <= index:
            pattern+="C"
            index-=faktor*1
        else: 
            pattern+="A"
    return pattern


def PatternToNumber(pattern):
    basenwerte = dict(A=0,C=1,G=2,T=3)
    numbers = list()
    pattern = pattern[::-1]
    for i in range(len(pattern)):
        base = pattern[i]
        wert = basenwerte[base]
        faktor = 4**i
        n = wert*faktor
        numbers.append(n)
    return sum(numbers)

def ComputingFrequencies (text,k):
    array = list()
    for i in range(4**k):
        array.append(0)
    for i in range(len(text)+1-k):
        kmer = text[i:i+k]
        index = PatternToNumber(kmer)
        array[index]+=1  
    return array
    
patterns = FasterFrequentWords ("ACGCGGCTCTGAAA",2)
print(patterns)