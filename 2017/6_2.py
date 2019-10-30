f=open("txtFile","r")

#Tell the least no of rows for the image to have a lateral symmetry

listy=[]

for line in f:

    listy.append(line.split(" "))



for i in range(200):

    listy[i][319]= listy[i][319][0:-1]


counter = 0

for j in range(200):
    
    for k in range(160):

        if listy[j][k]!=listy[j][319-k]:
            counter+=1
            break
        
print(counter)
