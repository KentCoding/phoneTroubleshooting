import sys
#Main Script
#User inputs their device type
device = input("What device is your issue related to? ")
#We then import the appropriate module for the user inputted device
if "phone" in device:
    import phone
elif "computer" in device:
    import computer #Module not in directory
elif "tablet" in device:
    import tablet #Module not in directory
else:
    print("Your device type is not supported. Please contact our technician.")

#Support query outside of conditional statement so may be used if no solution found inside solutionbank.
print("Sorry, we are unable to help you. Please fill in the form below for more support.")
#Enter user information so technician may contact the user.
firstName = input("First Name: ")
lastName = input("Last Name: ")
fullName = firstName + " " + lastName
phoneNumber = input("Phone Number: ")
#Open or create a text file for the case information
file = open("cases.txt","r")
#Set the case number (caseNo) variable to the last case number
#This requires the case file to have a '0' if no entries have been entered
#Then close the file
caseNo = file.readlines()[-1][0]
file.close()

#Increment the case number and set the value as a string so it may be written in the case file.
caseNo=int(caseNo)+1
caseNo=str(caseNo)

#Reopen the file and append the file with the additional contact information on the next avaliable line.
#Note the use of 'a' as the second parameter to append the file, rather than rewrite the file.
file=open("cases.txt","a")

#Write the content to the file and then close it.
file.write("\n"+caseNo+" "+fullName+" "+phoneNumber)
file.close()
print("Thank you for your query. We will be in touch.")
sys.exit()
