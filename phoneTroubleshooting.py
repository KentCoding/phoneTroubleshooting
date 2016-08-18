#Import Modules
import warnings
import string

#Define Globals
brands = ["apple", "android", "windows"]
brand = ''

def Main():
    init()
    print("--Welcome to Troubleshooting Applet--")
    print("In your query please include the brand of your device and the problem / symptom of your current issue. \n")
    query = input("Enter your query: ").lower()
    brand = set(brands).intersection(query.split())
    brand = ', '.join(brand)

    print(brand)
    
    if brand in brands:
        print("Exist")

def init():
    warnings.filterwarnings("ignore") #Disable while debugging

if __name__ == '__main__':
    Main()
