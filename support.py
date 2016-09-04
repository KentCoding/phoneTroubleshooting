import generic
#Issue Handler Module

def internalSupport(issue, question):
    if generic.userConfirm(question):
        if generic.userConfirm("Did this fix your issue?"):
            print("\nWe are glad we could help you.")
            generic.end()
        else:
            return
    else:
        print("Ok - not to worry.")
        if generic.userConfirm("Could you please try?"):
            return internalSupport(issue, question)
        else:
            generic.end()
            return
    return

def externalSupport(issue, skip, brand, query, ID):
    if skip == False:
        print("While we recognise your issue regarding your {0}, I'm afraid we cannot deal with this problem by default.".format(issue))
    if generic.userConfirm("Would you be happy to send your details to our technician?"):
        full_name = input("Enter your full name: ")
        user_email = input("Enter your email address: ")
        sendMessage(issue, brand, query, ID, full_name, user_email)
        generic.end()
    else:
        print("In this case, I am afraid we cannot help you. Please contact {0} - your manufacturer.".format(brand))
        generic.end()
    return

def sendMessage(issue, brand, query, ID, full_name, user_email):

    print("Sending.")
    
    import sys, os, re
    from smtplib import SMTP_SSL as SMTP
    from email.mime.text import MIMEText
    
    SMTPserver = 'SET SMTP SERVER ADDRESS'
    sender = user_email
    destination = ['SET DESTINATION EMAIL ADDRESS']

    USERNAME = "SET USERNAME"
    PASSWORD = "SET PASSWORD"

    text_subtype = 'plain'
    subject="Phone Troubleshooting Tech Support"
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

    try:
        print("Sending..")
        msg = MIMEText(content, text_subtype)
        msg['Subject']=       subject
        msg['From']   = sender # Some SMTP servers will do this automatically, not all
    
        conn = SMTP(SMTPserver)
        conn.set_debuglevel(False)
        conn.login(USERNAME, PASSWORD)
        try:
            conn.sendmail(sender, destination, msg.as_string())
        finally:
            conn.quit()
            print("Sending...")
            print("Sent.")
    
    except SMTPException:
        sys.exit( "mail failed; %s" % str(exc) ) #Error Exception Handler
