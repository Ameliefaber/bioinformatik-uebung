index = 45
k = 4
pattern = ""
for i in range(k):
    faktor = 4**(k-1-i)
    print (faktor)
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
print (pattern)
