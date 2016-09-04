#Import Modules
import os.path, warnings, generic, apple, android, windows

#Define Globals and Arrays
brands = ["apple", "android", "windows"]
brand = None

def init():
    #Define Module Settings
    #warnings.filterwarnings("ignore") #Disable for debugging
    ID = generic.generateID()
    #Main Menu
    print("--Welcome to Troubleshooting Applet--")
    print("In your query please include the brand of your device and the problem / symptom of your current issue. \n")
    return ID
    
def Main():
    ID = init()
    print("Case Number: {0}".format(ID))
    query = input("Enter your query: ").lower()
    print("")
    brand = selector(brands, query, "brand", "brands")
    solutions = solutionsImporter(brand, brands, "brand", "brands")
    issue = selector(solutions, query, "issue", "solutions")
    responseImporter(issue, brand, query, ID)
    generic.end()
    
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
    if generic.userConfirm("Would you like to redefine {0} and continue?".format(var_name)):
        return defineError(var, array, var_name, array_name)
    else:
        generic.end()

def defineError(var, array, var_name, array_name):
    var = input("Enter your device's {0}: ".format(var_name))
    int_cond = confirmIntersection(var, array)
    if int_cond == False:
        if generic.userConfirm("Try again?"):
            return defineError(var, array, var_name, array_name)
        else:
            generic.end()
    else:
        return var
##END Intersection Functions

##START Solution Queries Route
def solutionsImporter(var, array, var_name, array_name):
    int_cond = confirmIntersection(var, array)
    if int_cond == False:
        failedIntersection(var, array, var_name, array_name)
        return solutionsImporter(var, array, var_name, array_name)
    elif var == "apple":
        solutions = apple.solutions()
        return solutions
    elif var == "android":
        solutions = android.solutions()
        return solutions
    elif var == "windows":
        solutions = windows.solutions()
        return solutions
    return

def responseImporter(issue, brand, query, ID):
    if brand == "apple":
        apple.response(issue, brand, query, ID)
        return
    elif brand == "android":
        android.response(issue, brand, query, ID)
        return
    elif brand == "windows":
        windows.response(issue, brand, query, ID)
        return
    return
##END Solution Queries Route

if __name__ == '__main__':
    Main()
