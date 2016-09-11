##Import Modules
#Including custom modules for each potential brand and Object-Oritentated / Generic Functions to be used accross all modules.
import os.path, warnings, generic, apple, android, windows

##Define Globals and Arrays
#The array of 'brands' is used to identify is a query contains a brand which is supported by the application. The 'brand' variable is also defined as a global prior to its use.
brands = ["apple", "android", "windows"]
brand = None

def init():
    #Define and Setup Modules
    warnings.filterwarnings("ignore") #Disables Python warnings within the Python CLI. Disable for debugging.
    ID = generic.generateID() #Calls the generateID function from the custom generic module. See module for further information.
    #Initial Main Menu Interface
    print("--Welcome to Troubleshooting Applet--")
    print("In your query please include the brand of your device and the problem / symptom of your current issue. \n")
    return ID #Returns the ID that has been generated to the Main Function.
    
def Main():
    ID = init() #Sets the ID variable based on the returned variable from the init() sub procedure. While also setting up other modules and providing a CLI in the process.
    print("Case Number: {0}".format(ID)) #Print the Case ID, using a built-in format function.
    query = str(input("Enter your query: ").lower()) #User input for a issue query relating to their device with minor formatting, including a conversion to lowercase and setting a string foramt.
    print("") #Spacer in content prior to any further questions or solutions, dependant on the query entered.
    brand = selector(brands, query, "brand", "brands") #Set the brand variable based upon the selector() sub procedure. See function for further information.
    solutions = solutionsImporter(brand, brands, "brand", "brands") #Set the solutions array through importing the correct array based upon the brand selected. See function for further information.
    issue = selector(solutions, query, "issue", "solutions") #Set the issue using the selector() sub procedure with the parameters collected from the solutionsImporter() sub procedure.
    responseImporter(issue, brand, query, ID) #Call the custom response module to allow potential solutions to be given to the user.
    generic.end() #Call the end() sub procedure to end the program from the custom generic module.
    
##START Array Intersection Functions
def selector(array, query, var_name, array_name): #Pass the variables of the array, query and named titles of variables and arrays for the CLI.
    try: #Exception handler opening statement for any potential Pythonic error
        #Format Variable from Query
        var = set(array).intersection(query.split()) #Set the return variable to an intersecton between the provided query and array.
        var = ', '.join(var) #Format the return variable for an improved UI/UX
        #Check Condition After Setting
        int_cond = confirmIntersection(var, array) #Confirm if an intersection exists between variable and array. Then output a boolean result to allow error handling.
        if int_cond == False:
            raise NameError("No Intersection") #Call a named error exception handler
        return var #If successful, return the intersection between variable and array.
    except NameError:
        print("\nNo intersection found between query defined {0} and {1} array.\n".format(var_name, array_name))  #Provide a CLI in the event of an error
        return failedIntersection(var, array, var_name, array_name) # Provide the user an oppourtunity to redefine the variable to check against. Follow through to function for further information.

def confirmIntersection(var, array): #Check for an intersection between passed variable and array, then return boolean result.
    if var in array: #If statement to check for true result
        return True
    else:
        return False

def failedIntersection(var, array, var_name, array_name): #See summary below regarding passed parameters
    print("-{0} could not be found-".format(var_name.title())) #Print UI Information, using the formatting functions to include variables and manipulate variable to capitalise first letter.
    if generic.userConfirm("Would you like to redefine {0} and continue?".format(var_name)): #Check if user willing to continue and reattempt to enter a given variable
        return defineError(var, array, var_name, array_name) #If True (agreed), return to previous intersection function and reattempt with corrected function
    else:
        generic.end() #Else - End the program using generic module

##failedIntersection Sub Procedure Summary
#Call Structure (module_function)(function parameters)
#failedIntersection({1}, {2}, {3}, {4})  |  Handles the event of a failure to find intersection between given variable and array
#Parameter Structure:
#{1} | passes variable to function so that if required it may be rerouted to the next step
#{2} | passes array to function so that if required it may be rerouted to the next step
#{3} | passes variable name to function so that if required it may be rerouted to the next step
#{4} | passes array name to function so that if required it may be rerouted to the next step

def defineError(var, array, var_name, array_name): #See summary below regarding passed parameters
    var = input("Enter your device's {0}: ".format(var_name)) #User input with query printed with minor variable formatting
    int_cond = confirmIntersection(var, array) #Call confirmIntersection function for boolean result to check for intersection between variable and array
    if int_cond == False: #If intersection fails for a second time allow user to reattempt variable entry
        if generic.userConfirm("Try again?"): #Query to check if user wishes to continue
            return defineError(var, array, var_name, array_name) #Returns variable to the sub procedure defineError for a second time if the user wishes to try again
        else:
            generic.end() #Else the program is ended using generic module
    else:
        return var #Return corrected variable

##defineError Sub Procedure Summary
#Call Structure (module_function)(function parameters)
#defineError({1}, {2}, {3}, {4})  |  Handles the event of a failure where the user is going to redefine the variable for evaluation
#Parameter Structure:
#{1} | passes variable to function so that if required it may be rerouted to the next step
#{2} | passes array to function so that if required it may be rerouted to the next step
#{3} | passes variable name to function so that if required it may be rerouted to the next step
#{4} | passes array name to function so that if required it may be rerouted to the next step
##END Array Intersection Functions

##START Solution Queries Route
def solutionsImporter(var, array, var_name, array_name): #See summary below regarding passed parameters
    int_cond = confirmIntersection(var, array) ##START of Second and last intersection check prior to setting the solutions array
    if int_cond == False:
        failedIntersection(var, array, var_name, array_name)
        return solutionsImporter(var, array, var_name, array_name) ##END
    elif var == "apple": #If brand equal 'apple' set solutions array to the apple array from the solutions function within apple module
        solutions = apple.solutions()
        return solutions #Once completed return the array for the next step
    elif var == "android": #If brand equal 'android' set solutions array to the android array from the solutions function within android module
        solutions = android.solutions()
        return solutions #Once completed return the array for the next step
    elif var == "windows": #If brand equal 'windows' set solutions array to the windows array from the solutions function within windows module
        solutions = windows.solutions()
        return solutions #Once completed return the array for the next step
    return

##solutionsImporter Sub Procedure Summary
#Call Structure (module_function)(function parameters)
#solutionsImporter({1}, {2}, {3}, {4})  |  Handles the import of the correct array from a varying module dependant on the user-selected brand
#Parameter Structure:
#{1} | passes variable to function so that if required it may be rerouted to the next step
#{2} | passes array to function so that if required it may be rerouted to the next step
#{3} | passes variable name to function so that if required it may be rerouted to the next step
#{4} | passes array name to function so that if required it may be rerouted to the next step

def responseImporter(issue, brand, query, ID): #See summary below regarding passed parameters
    if brand == "apple": #Dependant on brand select a module to call and request the response sub procedure. See module for more information.
        apple.response(issue, brand, query, ID)
        return
    elif brand == "android":
        android.response(issue, brand, query, ID)
        return
    elif brand == "windows":
        windows.response(issue, brand, query, ID)
        return
    return

##responseImporter Sub Procedure Summary
#Call Structure (module_function)(function parameters)
#solutionsImporter({1}, {2}, {3}, {4})  |  Handles the selection of response queries based upon brand using passed variables
#Parameter Structure:
#{1} | passes the issue for the response module to be used to select the potential solution route and for the support ticket system
#{2} | passes the brand to be used for module selection and for the support ticket system
#{3} | passes the query for the support ticket system
#{4} | passes the ID for the support ticket system
##END Solution Queries Route

if __name__ == '__main__':
    Main()
