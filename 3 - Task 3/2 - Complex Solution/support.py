##Import Modules
#Including custom module for generic functions and warnings module to handle SMTP debugging.
import generic, warnings, time

DEBUG_MODE = True

#Issue Handler Module

def internalSupport(issue, question): #UI for each defined response upon calling from brand module
    if generic.userConfirm(question): #Request if user has attempted this line of query
        if generic.userConfirm("Did this fix your issue?"): #If so, then ask if the issue has been fixed
            print("\nWe are glad we could help you.")
            generic.end() #Therefore, end program using end sub procedure from generic module
        else:
            return #If issue still not fixed, then continue to next line of query
    else:
        print("Ok - not to worry.") #If the user has not attempted the query, then ask if they will.
        if generic.userConfirm("Could you please try?"):
            return internalSupport(issue, question) #Repeat the question if user agreed to reattempt
        else:
            generic.end() #Else quit the program
            return
    return

def externalSupport(issue, skip, brand, query, ID):
    if skip == False: #Skip element of UI dependant on type of external support required
        print("While we recognise your issue regarding your {0}, I'm afraid we cannot deal with this problem by default.".format(issue)) #Format UI with 'issue' variable
    if generic.userConfirm("Would you be happy to send your details to our technician?"): #Request if user happy to send details to a technician
        full_name = input("Enter your full name: ") #Enter full name for technician email
        user_email = input("Enter your email address: ") #Enter user's email address for technician email
        sendMessage(issue, brand, query, ID, full_name, user_email) #Call sendMessage function to send the email with parameters required
        generic.end() #Once email sent, end the program
    else: #If not and no solution found, refer user to manufacturer.
        print("In this case, I am afraid we cannot help you. Please contact {0} - your manufacturer.".format(brand))
        generic.end() #End the program
    return

def messageSent():
    print("WARNING: DEBUG MODE ACTIVE")
    print("Sending.")
    print("Sending..")
    print("Sending...")
    generic.end()

def sendMessage(issue, brand, query, ID, full_name, user_email):
    if DEBUG_MODE == True:
        messageSent()
    #Start UI Loading CLI
    print("Sending.")

    #Import required modues for SMTP Server Messages, SSL and MIME text formatting
    import sys, os, re 
    from smtplib import SMTP_SSL as SMTP
    from email.mime.text import MIMEText

    #Define Server Connection Details
    SMTPserver = 'SET SMTP SERVER ADDRESS'
    sender = user_email
    destination = ['SET DESTINATION EMAIL ADDRESS']

    USERNAME = "SET USERNAME"
    PASSWORD = "SET PASSWORD"

    #Set text_subtype, in this case 'plain text', or you could use something like 'HTML'
    text_subtype = 'plain'
    subject="Phone Troubleshooting Tech Support" #Define the subject header for the email
    #Style and Structure the contents of the email message which will include all of the client information using the format function
    content="""\
    Here is a support requst ticket from {0}. Please see enclosed data.
    
    Client Name: {0}
    Client Email Address: {1}
    Case ID: {2}
    
    --Quick Summary--
    Client's brand of device: {3}
    Client's issue: {4}
    
    --Inital Query from Client--
    {5}
    """.format(full_name, user_email, ID, brand, issue, query)

    try: #Attempt to send the email and support exception handlers
        #Continue UI Loading CLI
        print("Sending..")
        msg = MIMEText(content, text_subtype) #Set the message to the given content and format it according to the MIME requirements
        msg['Subject'] = subject #Set the message subject, as defined earlier
        msg['From'] = sender #Set sender email address, if supported by SMTP server
    
        conn = SMTP(SMTPserver) #Define a connection attribute relating to the SMTP server connection
        conn.set_debuglevel(False) #Disable SMTP status messages to handle them manually using exceptions
        conn.login(USERNAME, PASSWORD) #Connect to the SMTP server using defined username and password
        try:
            conn.sendmail(sender, destination, msg.as_string()) #Attempt to send the email
        finally: #Once completed the sending of the given email complete the following
            conn.quit() #Close the connection to the server
            #End UI Loading CLI
            print("Sending...")
            print("Sent.")
    except smtplib.SMTPException: #Provide error exception for Unknown SMTP Authentcation Error
        warnings.warn("Failed Connection") #Provide warning for debugging - dependant on setting within main program
        print("Unknown SMTP Authentcation Error")
        pass
    except smtplib.SMTPAuthenticationError: #Provide error exception for SMTPAuthenticationError
        warnings.warn("Failed Connection") #Provide warning for debugging - dependant on setting within main program
        print("Server rejected username/password combination")
        pass
    except smtplib.SMTPConnectError: #Provide error exception for SMTPConnectError
        warnings.warn("Failed Connection") #Provide warning for debugging - dependant on setting within main program
        print("Failure to connect to server")
        print("At this time we cannot help you. Pleas try again later or contact {0} - your manufacturer.".format(brand))
        pass
    except ConnectionRefusedError: #Provide error exception for ConnectionRefusedError
        warnings.warn("Failed Connection") #Provide warning for debugging - dependant on setting within main program
        print("Failure to connect to server")
        print("At this time we cannot help you. Pleas try again later or contact {0} - your manufacturer.".format(brand))
        pass
    
#sendMessage Sub Procedure Summary
#Call Structure (module_function)(function parameters)
#sendMessage({1}, {2}, {3}, {4}, {5}, {6})  |  Handles the sending of messages using passsed paramters to the technician
#Parameter Structure:
#{1} | Passes the issue for the email
#{2} | Passes the brand for the email
#{3} | Passes the query for the email
#{4} | Passes the ID for the email
#{5} | Passes the full_name for the email and dependant on the SMTP Server, use as the sender credentials.
#{6} | Passes the user_email for the email and dependant on the SMTP Server, use as the sender credentials.
