basenwerte = dict(A=0,C=1,G=2,T=3)
print (basenwerte)
pattern = "AGT"
numbers = list()
pattern = pattern[::-1]
for i in range(len(pattern)):
    base = pattern[i]
    wert = basenwerte[base]
    faktor = 4**i
    n = wert*faktor
    numbers.append(n)
lösung = sum(numbers)
print (lösung)
    
    
