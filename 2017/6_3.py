
f=open("/Users/Looky/Desktop/Dane_PR2/przyklad.txt","r")


# Count cotrasitng pixels

listy=[]

for line in f:

    listy.append(line.split(" "))



for i in range(200):

    listy[i][319]= listy[i][319][0:-1]





counter =0

for j in range(200):

    for k in range(320):

        if k==0 and j!=0 and j!=199:
            if abs(int(listy[j][k+1])-int(listy[j][k]))>128 or abs(int(listy[j+1][k])-int(listy[j][k]))>128 or abs(int(listy[j-1][k])-int(listy[j][k]))>128:
                counter+=1

        elif k==319 and j!=0 and j!=199 :
            if abs(int(listy[j][k-1])-int(listy[j][k]))>128 or abs(int(listy[j+1][k])-int(listy[j][k]))>128 or abs(int(listy[j-1][k])-int(listy[j][k]))>128:
                counter+=1

            
        elif j==0 and k!=0 and k!=319:
            if abs(int(listy[j][k+1])-int(listy[j][k]))>128 or abs(int(listy[j][k-1])-int(listy[j][k]))>128 or abs(int(listy[j+1][k])-int(listy[j][k]))>128:
                counter+=1


        elif j==199 and k!=0 and k!=319:
            if abs(int(listy[j][k+1])-int(listy[j][k]))>128 or abs(int(listy[j][k-1])-int(listy[j][k]))>128 or abs(int(listy[j-1][k])-int(listy[j][k]))>128:
                counter+=1

        elif k==0 and j==0:
            if abs(int(listy[j][k+1])-int(listy[j][k]))>128 or abs(int(listy[j+1][k])-int(listy[j][k]))>128:
                counter+=1

        elif k==0 and j==199:
            if abs(int(listy[j][k+1])-int(listy[j][k]))>128 or abs(int(listy[j-1][k])-int(listy[j][k]))>128:
                counter+=1

        elif k==319 and j==0:
            
            if abs(int(listy[j][k-1])-int(listy[j][k]))>128 or abs(int(listy[j+1][k])-int(listy[j][k]))>128:
                counter+=1

        elif k==319 and j==199:
            if abs(int(listy[j][k-1])-int(listy[j][k]))>128 or abs(int(listy[j-11][k])-int(listy[j][k]))>128:
                counter+=1

        else:

            if abs(int(listy[j][k+1])-int(listy[j][k]))>128 or abs(int(listy[j][k-1])-int(listy[j][k]))>128 or abs(int(listy[j+1][k])-int(listy[j][k]))>128 or abs(int(listy[j-1][k])-int(listy[j][k]))>128:
                counter+=1


print(counter)
