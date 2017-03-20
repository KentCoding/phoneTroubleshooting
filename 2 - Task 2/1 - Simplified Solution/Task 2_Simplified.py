#Read the text file 'solutions.txt.' and save it as the variable 'database'
database=open("solutions.txt","r")
#User inputs a response to the question
issue=input("What is the problem? ")

#Using a chain of conditional statements
#We may evaluate whether a keyword appears in the user input.
#If a keyword does appear we may read the textfile.
#When reading the textfile we only read the line appropriate for the solution.
if "phone" in issue and "display" or "screen" in issue:
    #We print the line from the textfile.
    print(database.readlines()[0])
    #Once read, we must close the file.
    database.close()
elif "phone" in issue and "battery" or "power" in issue:
    print(database.readlines()[1])
    database.close()
else:
    print("No solution found.")
    database.close()
