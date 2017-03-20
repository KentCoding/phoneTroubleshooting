import sys, string
questionArray = ["Have you tried plugging in your device?", "Have you tried turning on your device?"]
noOfQuestions = len(questionArray)
device = "iPhone"
#Note the use of {0} and .format(variable_name) later, this is a useful function to allow text formatting within a question to ensure it is gramatically correct.
#In this example, the script is made generic for a range of different devices.
i=0

def userConfirm(question): #Require the user to confirm a qustion and return a boolean result
    reply = str(input(question+' (y/n): ')).lower().strip() #User input a question; convert to lower case; then strip to individual characters
    if reply[0] == 'y': #Check first character for 'y'
        return True #If so, return True
    if reply[0] == 'n': #Check first character for 'n'
        return False #If so, return False
    else: #Else return the user once again to the userConfirm sub procedure
        return userConfirm("Please confirm using yes or no")

def end(): #End sub procedure which adds an additional UI feature prior to ending the program
    print("Have a good day. Bye.")
    sys.exit()

#We need to use a function to avoid redundant code by reqriting the statement that asks the question many times. The while loop calls this function and passes the value i to provide the appropriate question from the array.
def questionLoop(i):
    question = str(questionArray[i])
    if userConfirm(question):
        if userConfirm("Is your {0} now working?".format(device)):
            print("Glad we could help.")
            end()
    else:
        print("Please try the potential solution.")
        questionLoop(i)

#This while loop follows the condition that if the index is less than the number of questions in the array then continue asking the questions
while i < noOfQuestions:
    questionLoop(i)        
    i += 1 #Increment the loop by one then restart
    
#As there is no indentation this statement will run once the array has been completed and there are no more questions. If the problem is fixed we call an end() function which handles the end of the script.
print("I'm afraid we do not have a solution for you.")
end()
