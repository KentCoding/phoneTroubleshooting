#Import Modules
import sys, warnings, string

#Define Globals
brands = ["apple", "android", "windows"]
brand = None

def init():
    #Define Imported Module Settings
    warnings.filterwarnings("ignore") #Disable for debuggings
    #Main Menu
    print("--Welcome to Troubleshooting Applet--")
    print("In your query please include the brand of your device and the problem / symptom of your current issue. \n")

def Main():
    init()
<<<<<<< HEAD
    if brand None:
        query = input("Enter your query: ").lower()
    else:
        print("Brand Selected, Only problem query")
=======
    query = input("Enter your query: ").lower()
>>>>>>> master
    
    brand = brandSelector(query)
    print(brand)

#Code Infrastructure and Modules
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
        raise

def confirmIntersection(brand):
    if brand in brands:
        #print("True") #Debug Check
        return True
    else:
        #print("False") #Debug Check
        return False

if __name__ == '__main__':
    Main()
