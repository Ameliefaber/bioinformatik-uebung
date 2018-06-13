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
  

Pattern = "AAA"
Dna = ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]

result = DistanceBetweenPatternAndStrings (Pattern, Dna)
print (result)

