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
    brand = brandSelector(query)
    keywordSelection(query, brand)

##START Brand Selection Route
def brandSelector(query):
    try:
        #Format Brands Query
        brand = set(brands).intersection(query.split())
        brand = ', '.join(brand)
        #Check Condition After Setting
        int_cond = confirmIntersection(brand)
        if int_cond == False:
            raise NameError("No Intersection")
        return brand
    except NameError:
        print("\nNo Intersection found between query defined brand and brands array\n")
        return brandDetectionFailure()

def confirmIntersection(brand):
    if brand in brands:
        return True
    else:
        return False
##END Brand Selection Route

##START Brand Selection Route | SUB: Failed Selection
def brandDetectionFailure():
    print("-Brand could not be found-")
    print("Query still stored for your issue")
    if userConfirm("Would you like to redefine a brand and continue?"):
        return defineBrand()
    else:
        end()

def defineBrand():
    brand = input("Enter your device's brand: ")
    int_cond = confirmIntersection(brand)
    if int_cond == False:
        if userConfirm("Try again?"):
            defineBrand()
        else:
            end()
    else:
        print("End of Sub Route") #STILL NEEDS WORK
        return brand
##END Brand Selection Route | SUB: Failed Selection

##START Keyword Selection Route
def keywordSelection(query, brand):
    print("Keyword Selector") #START Debugging Section
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
