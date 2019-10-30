f=open("/Users/Looky/Desktop/Dane_PR2/przyklad.txt","r")

# Longest column of the same length pixels

listy=[]

for line in f:

    listy.append(line.split(" "))



for i in range(200):

    listy[i][319]= listy[i][319][0:-1]



maxi=1
counter=1

for k in range(320):

    col=listy[0][k]
    

    for j in range(1,200):

        if col==listy[j][k]:
            counter+=1

        else:
            if counter>maxi:
                maxi=counter

            counter=1
            col=listy[j][k]


print(maxi)
            



            

        

        
