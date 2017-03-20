#Android Solutions and Response Handlers
def solutions():
    solutions = ["screen", "battery", "speaker", "alert", "slider"] #Define array for given brand upon calling.
    return solutions

def response(issue, brand, query, ID): #Handler which provides responses for given issues upon calling within main script.
    issueStatus = issueHandler(issue, brand, query, ID) #Set a boolean variable from calling the issue handler in the event of an error and give an appropriate response.
    if issueStatus == True:
        print("\nWe are glad we could help you.")
    else:
        print("Sorry we could not fix your issue.")
    return

def issueHandler(issue, brand, query, ID): #Issue Handler function from response module
    import support #import Support module to handle questions and case number output in event of no solution.
    if issue == "screen": #Check for issue to provide potential solution
        support.externalSupport(issue, False, brand, query, ID) #Call support module to handle reponse.
        return True
    elif issue == "battery":
        support.internalSupport(issue, "Have you tried plugging in your Android phone?")
        support.externalSupport(issue, True, brand, query, ID)
        return True
    elif issue == "speaker":
        support.internalSupport(issue, "Have you ensured any headphones are removed?")
        support.internalSupport(issue, "Have you tried to reset your Android phone to eliminate OS issues?")
        support.externalSupport(issue, True, brand, query, ID)
        return True
    elif issue == "alert" or "slider": #Example handler for multiple naming scenarios - see added array elements.
        support.internalSupport(issue, "Have you checked to see if you can move the slider position?")
        support.internalSupport(issue, "Have you checked to see if the alert slider interacts with the GUI?")
        support.internalSupport(issue, "Have you attempted to reset the device to elimiate OS issues?")
        support.externalSupport(issue, True, brand, query, ID)
        return True
    else: #Handles issues without a set response.
        support.externalSupport(issue, False, brand, query, ID)
        return False

    ###Support Module Response Handler Summary
    ##Call Structure(module).(module_function)(function parameters)
    #
    ##support.internalSupport({1}, {2})   |   Handles the event of a potential solution to issue
    #Parameter Structure:
    #{1} | passes issue of device to module
    #{2} | passes question to query the user
    #
    ##support.externalSupport({1}, {2}, {3}, {4}, {5})   |   Handles the event of no solutions to issue
    #Parameter Structure:
    #{1} | passes issue of device to module
    #{2} | gramatical change in the event that no potential solutions were found without any checks.
    #{3} | passes brand for Technician Support Message
    #{4} | passes query for Technician Support Message
    #{5} | passes ID for Technician Support Message
