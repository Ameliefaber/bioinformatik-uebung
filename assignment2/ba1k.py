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



text = "ACGCGGCTCTGAAA"
k = 2
array = list()
for i in range(4**k):
    array.append(0)
for i in range(len(text)+1-k):
    kmer = text[i:i+k]
    index = PatternToNumber(kmer)
    array[index]+=1
print(array)   
    
    
