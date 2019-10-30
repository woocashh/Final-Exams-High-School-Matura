
# Split file into list of words. 

file=open("‎⁨⁩txtFile","r")


listy=[]

for line in file:


    listy.append(line.split(" "))


print(listy[0:10])
