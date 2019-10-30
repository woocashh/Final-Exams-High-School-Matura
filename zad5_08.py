file=open("txtFile","r")

listy=[]



for line in file:

    listy.append(str(line[0:-1]))



def ispalindrome(x):

    if len(x)==1:

        return True


    elif len(x)%2==0:


        for i in range(len(x)//2):

            if x[i]!=x[-1-i]:

                return False

    elif len(x)%2==1:

        for i in range((len(x)-1)//2):

            if x[i]!=x[-1-i]:

                return False


    return True


            
newlist=[]




for i in listy:


    word1=""
    word2=""

    for j in range(len(i)):

        if i[-1-j]==i[0]:

            if ispalindrome(i[0:len(i)-j]):

                word1=i[0:len(i)-j]
                word2=i[len(i)-j:]
                break

            

    rword2=""
        
    for k in range(len(word2)):

        rword2+=word2[-1-k]


    newlist.append(rword2+word1+word2)



            

filey=open("hasla_b.txt","w")

for line in newlist:

    filey.write(line+"\n")


filey.close()



sumy=0

maxi=0

maxind=0

mini=100

minind=0

lis12=[]


for i in range(len(newlist)):

    sumy+=len(newlist[i])


    if len(newlist[i])>maxi:

        maxi=len(newlist[i])
        maxind=i


    if len(newlist[i])<mini:

        mini=len(newlist[i])
        minind=i


    if len(newlist[i])==12:

        lis12.append(newlist[i])

        
print(lis12)
print(newlist[maxind])
print(newlist[minind])
print(sumy)

                


                


                

                


            

        

        


    
