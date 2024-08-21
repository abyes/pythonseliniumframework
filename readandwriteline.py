file =open("readandwrite.txt")
#with open("readandwrite.txt") as file:  #if i use this line so i dont need file.open and close both
#print(file.read())  #this will read all the content
#print(file.readline()) #this will read only the first line
#print(file.readline(2))  #this will read only the first two words of first line
#print(file.read(5)) #this will read all the 2 starting charcater from every line

#a=file.readline()
#while a!="":
    #print(a)
    #a = file.readline()

file =file.readlines() #this is like array u can give the range how many u want to print
for loop in file:
    print(loop)



  #this will make sure that there is no memory leakage