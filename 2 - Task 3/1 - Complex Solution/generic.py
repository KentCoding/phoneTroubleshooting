##Import Modules
#Including sys, string and random functions to manipulate data within functions as seen below
import sys, string, random
#Generic Functions Module
def userConfirm(question): #Require the user to confirm a qustion and return a boolean result
    reply = str(input(question+' (y/n): ')).lower().strip() #User input a question; convert to lower case; then strip to individual characters
    if reply[0] == 'y': #Check first character for 'y'
        return True #If so, return True
    if reply[0] == 'n': #Check first character for 'n'
        return False #If so, return False
    else: #Else return the user once again to the userConfirm sub procedure
        return userConfirm("Please confirm using yes or no")

def generateID(): #Return a string consisting of two triplets of Uppercase ASCII followed by digits to set as a unique identifier for when being sent to the technician
    return "".join([random.choice(string.ascii_uppercase) for i in range(3)])+"-"+"".join([random.choice(string.digits) for i in range(3)])

def end(): #End sub procedure which adds an additional UI feature prior to ending the program
    print("Have a good day. Bye.")
    sys.exit()
