file = open("txtFile", "r")

# Count the number of palindromes in a list

words=[]
for line in file:
    words.append(line[0:-1])


outcome=0


for i in words:


    if len(i)==1:

        outcome+=1

    else:

        if len(i)%2==1:

            for k in range(0,(len(i)-1)//2):

                if i[k]!=i[-1-k]:

                    outcome-=1

                    break

            outcome+=1

        elif len(i)%2==0:

            for k in range(0,int(len(i)/2)):

                if i[k]!=i[-1-k]:

                    outcome-=1

                    break

            outcome+=1

print(outcome)

            


    

    
