def sortString(inputString):
    character=list(inputString)
    n=len(character)
    for i in range(0,n):
     for j in range(0,n-1):
        if character[j]>character[j+1]:
           character[j],character[j+1]=character[j+1],character[j]
    sortedString="".join(character)      
    return sortedString




inputString="ambuj"
print(sortString(inputString))
    

