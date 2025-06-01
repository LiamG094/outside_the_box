import time 
#starting prompt to get the username

print ("----------OUTSIDE THE BOX----------")
time.sleep(1)

time.sleep(1)


def main_menu():
    user = input ("Please enter your username ")
    print("Welcome to Outside The Box, " + user + "!")
    time.sleep(1)
    print("Type HELP for instructions and START to begin.")
    
    option = input("What would you like to do? ").strip().upper()  # Clean input
    
    if option == "HELP":
        print("Here are the instructions...")
    elif option == "START":
        print("Starting the game...")
    else:
        print("Please enter a valid option.")

main_menu()

#if option is "HELP" print the instructions
#if options is START - Print game intro 
