def MedianString (k,Dna):
    mindistance = 1000000000000
    for i in range(4**k):
        kmer = NumberToPattern (i,k)
        distance = DistanceBetweenPatternAndStrings (kmer, Dna)
        if distance < mindistance:
            mindistance = distance
            minkmer = kmer
    return minkmer 
        
        
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
  
    
def DistanceBetweenPatternAndStrings (Pattern, Dna):
    distance = 0

    for text in Dna:
        distance += DistanceBetweenPatternAndString (Pattern, text)
    return distance

def DistanceBetweenPatternAndString (Pattern, text):
    k = len(Pattern)
    mindistance = 1000000000
    for i in range(len(text)+1-k):
        kmer = text [i:i+k]   
        distance = HammingDistance (kmer,Pattern)
        if distance < mindistance:
            mindistance = distance
    return mindistance
        
def HammingDistance (a, b):
    distance = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            distance += 1
    return distance
  
    
k = 3
Dna = ["AAATTGACGCAT", 
       "GACGACCACGTT", 
       "CGTCAGCGCCTG", 
       "GCTGAGCACCGG", 
       "AGTACGGGACAG"]

MedianString (k,Dna)
result = MedianString (k,Dna)
print (result)