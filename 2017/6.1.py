f=open("txtFile","r")

# Find the most and the least bright pixel in an image
listy=[]

for line in f:

    listy.append(line.split(" "))



for i in range(200):

    listy[i][319]= listy[i][319][0:-1]



maxi=0
mini=255

for k in range(200):

    for j in range(320):

        if int(listy[k][j])<mini:
            mini = int(listy[k][j])

        if int(listy[k][j])>maxi:
            maxi= int(listy[k][j])



f1=open("/Users/Looky/Desktop/Dane_PR2/wyniki6_1.txt", "w")


f1.write("Max: "+str(maxi)+"\n")
f1.write("Min: "+ str(mini)+"\n")
f1.close()
