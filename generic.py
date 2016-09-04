import sys, string, random
#Generic Functions Module
def userConfirm(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return userConfirm("Please confirm using yes or no")

def generateID():
    return "".join([random.choice(string.ascii_uppercase) for i in range(3)])+"-"+"".join([random.choice(string.digits) for i in range(3)])

def end():
    print("Have a good day. Bye.")
    sys.exit()
