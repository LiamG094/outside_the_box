import time 
#starting prompt to get the username

print ("----------OUTSIDE THE BOX----------")
time.sleep(1)
user = input ("Please enter your username ")
time.sleep(2)
print("Welcome to Outside The Box, " + user + "!")
time.sleep(2)

#User selects an option from the main menu to proceed

main_menu = ("----------MAIN MENU----------") # could this be an object ??? 
print (main_menu)
print("HELP - instructions ")
print("START - start the game ")
option = input("Select an option: ")

#if option is "HELP" print the instructions
#if options is START - Print game intro 
