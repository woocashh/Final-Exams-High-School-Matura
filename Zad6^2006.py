file = open("FILE", "r")


# Count how many words show up more than 2 times in a list, 
# and what is the most abundant word

words=[]
for line in file:
    words.append(line[0:-1])

dicty={}



howmany=0

for i in words:

    try:

        dicty[i]+=1
        if dicty[i]==2:
            howmany+=1

        if  dicty[i]==30:

            top=i

    except KeyError:

        dicty[i]=1



print("Słowa ktore wiecej niz raz: "+str(howmany)+" Słowo top: "+i+" "+str(max(dicty.values())))
    
    
