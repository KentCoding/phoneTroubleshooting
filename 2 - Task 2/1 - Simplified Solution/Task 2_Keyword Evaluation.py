#User inputs a response
issue = input("What is your problem? ")

#We check whether any of the words in their query
#are a keyword in the conditional statement.
if "display" in issue:
    print("Display related problem.")
else:
    print("No solution found)")
