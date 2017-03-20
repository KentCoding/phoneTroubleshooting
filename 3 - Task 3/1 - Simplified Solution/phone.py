#Phone Solutionbank Module
#Import 'sys' module to cleanly end the script
import sys

#We may place a tree of solutions here for the given device.
issue = input("What is your problem? ")
if "display" in issue:
    print("Display issue solution.")
    #Solution path with information on how to fixs
    sys.exit()
else:
    #Exit path to technician support
    print("No solution found.")

#If there is no solution then the user is directed towards the support script
