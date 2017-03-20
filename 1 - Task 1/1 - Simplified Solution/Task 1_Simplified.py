import sys #A module which allows you to cleanly end the program.
issue = input("What part of your device is not working? ") #Ask the user a question regarding their device's issue.

#You may repeat this section for different types of issues, for example, you may add 'power' or 'buttons'.
# -- START of Display Category -- #
if "display" or "screen" in issue:
    #Using a tree of question, we may ask additional questions.
    #The reponses are stripped and made lowercase so we may quickly identify whether the user reponds 'yes' or 'no'.
    reply = str(input("Is your display showing a picture? (y/n) ")).lower().strip()
    if reply[0] == 'y':
        reply = str(input("Is the screen detecting touch? (y/n) ")).lower().strip()
        if reply[0] == 'y':
            print("Please contact your supplier, as there is no quick solution for your issue.")
            sys.exit()
        if reply[0] == 'n':
            #If we reach a point where we may offer precise advice, then we may do so.
            print("It sounds like the digitiser is broken, please take your device to the supplier.")
    elif reply[0] == 'n':
        print("It seems your screen panel needs replacing, please take your device to the supplier.")
    else:
        print("Please respond using yes or no.")
        sys.exit()
# -- END of Display Category -- #

#If there is no category found then refer the user to the supplier.
else:
    print("I'm afraid we have no solutions for you.")
    print("Please contact your supplier.")
    sys.exit()
