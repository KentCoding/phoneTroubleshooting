#Import Modules
import warnings
import string
import sys

#Define Globals
brands = ["apple", "android", "windows"]
brand = ''

def Main():
    init()
    print("--Welcome to Troubleshooting Applet--")
    print("In your query please include the brand of your device and the problem / symptom of your current issue. \n")

    query = input("Enter your query: ").lower()
    brand = brandSelector(query)
    print(brand)
    
    if brand in brands:
        print("Exist")

def brandSelector(query):
    try: 
        brand = set(brands).intersection(query.split())
        brand = ', '.join(brand)
        return brand
    except error:
        print("Brand does not exist")

def init():
    warnings.filterwarnings("ignore") #Disable while debugging

if __name__ == '__main__':
    Main()
