#Import Modules
import sys, warnings, string

#Define Globals
brands = ["apple", "android", "windows"]
brand = None

def init():
    #Define Module Settings
    warnings.filterwarnings("ignore") #Disable for debugging
    #Main Menu
    print("--Welcome to Troubleshooting Applet--")
    print("In your query please include the brand of your device and the problem / symptom of your current issue. \n")

def Main():
    init()
    query = input("Enter your query: ").lower()
    brand = selector(brands, query, "brand", "brands")
    keywordSelection(query, brand)
    
##START Intersection Functions
def selector(array, query, var_name, array_name):
    try:
        #Format Variable from Query
        var = set(array).intersection(query.split())
        var = ', '.join(var)
        #Check Condition After Setting
        int_cond = confirmIntersection(var, array)
        if int_cond == False:
            raise NameError("No Intersection")
        return var
    except NameError:
        print("\nNo intersection found between query defined {0} and {1} array.\n".format(var_name, array_name)) 
        return failedIntersection(var, array, var_name, array_name)

def confirmIntersection(var, array):
    if var in array:
        return True
    else:
        return False

def failedIntersection(var, array, var_name, array_name):
    print("-{0} could not be found-".format(var_name.title()))
    if userConfirm("Would you like to redefine {0} and continue?".format(var_name)):
        return defineError(var, array, var_name, array_name)
    else:
        end()

def defineError(var, array, var_name, array_name):
    var = input("Enter your device's {0}: ".format(var_name))
    int_cond = confirmIntersection(var, array)
    if int_cond == False:
        if userConfirm("Try again?"):
            return defineError(var, array, var_name, array_name)
        else:
            end()
    else:
        return var
##END Intersection Functions

##START Keyword Selection Route
def keywordSelection(query, brand):
    print("---TEST PASSED---") #START Debugging Section
    print("Your query:", query) 
    print("Your brand:", brand) #END Debugging Section
##END Keyword Selection Route

##START Generic Functions
def userConfirm(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return userConfirm("Please confirm using yes or no")

def end():
    print("Have a good day. Bye.")
    sys.exit()
##END Generic Functions

if __name__ == '__main__':
    Main()
