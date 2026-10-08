# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 4
# Author Name: 
# Date: 

# SCENARIO
# You are developing a registration system for a small event
# The organizers have a list of registered attendees and need to check whether someone is permitted to enter.

registered_guests = [
    "Alice",
    "Bob"
]
checked_guest = []


# TODO 1: Create a while loop thap that continues until all guests are checked in.

while len(registered_guests) > 0:

    # TODO 2: Ask the user to enter their name
    check = input("Hello what is your name? : ")
  
    # TODO 3: Iterate through guest list and check whether their name appears in the registered guests list
    if check in registered_guests:
        # TODO 4: If registered and they're not already in checked in, add their name to the checked-in list and print a welcome message
        print(f"Welcome {check}!")
        checked_guest.append(registered_guests.pop(registered_guests.index(check)))
        # TODO 5: Otherwise, Display an appropriate message for unregistered guests
    else:
        print(f"Sorry {check}, your name is not in the list")
        
    print(f"Checked in guests {checked_guest}")


# TODO 7: Print a message telling us that all guests have successfully checked in!
print("All guests have been checked in!")




    

    





# EXPECTED OUTPUT:
# [ "Alice", "Bob"]
# What is your name:  "Alice"
#    Welcome Alice!
#    Checked In Guests: [ Alice ]
# What is your name:  "Fred"
#    Sorry Fred, your name isn't on the list.
#    Checked In Guests: [ Alice ]
# What is your name:  "Bob"
#    Welcome Bob!
#    Checked In Guests: [ Alice, Bob ]
# All guests have been checked in!
