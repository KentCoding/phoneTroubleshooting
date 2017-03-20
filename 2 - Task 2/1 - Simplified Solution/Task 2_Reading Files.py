#Read the text file 'solutions.txt.' and save it as the variable 'database'
#The second parameter 'r'instructs the functon to 'read' the file
database=open("solutions.txt","r")

#We may then print the data on a given line.
#Remembering that to read line one, the index number is zero, see below.
print(database.readlines()[0])

#Upon completion of the function, we may then close the file.
database.close()
