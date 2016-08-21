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
    brand = selector(brands, query)
    keywordSelection(query, brand)

def selector(array, query):
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
        print("\nNo intersection found between query defined variable and {0} array.".format("xyz")) 
        return failedIntersection(var, array)

def confirmIntersection(var, array):
    if var in array:
        return True
    else:
        return False

def failedIntersection(var, array):
    print("-Intersection could not be found-")
    if userConfirm("Would you like to redefine and continue?"):
        return defineError(var, array)
    else:
        end()

def defineError(var, array):
    var = input("Enter: ")
    int_cond = confirmIntersection(var, array)
    if int_cond == False:
        if userConfirm("Try again?"):
            return defineError()
        else:
            end()
    else:
        return var

##START Keyword Selection Route
def keywordSelection(query, brand):
    print("---TEST PASSED---") #START Debugging Section
    print("Your query: ", query) 
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
