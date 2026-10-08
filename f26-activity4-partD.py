# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 4
# Author Name: 
# Date: 

# SCENARIO
# A restauraunt wants a simple ordering system that allows customers to browse a menu, select items, and calculate their total bill.

menu  = {
    "Burger" : 12.00,
    "Pizza" : 15.00,
    "Salad" : 9.00,
    "Fries" : 5.00,
    "Drink" : 3.00
}

order = []


print("Main Menu")

# TODO 1: Print out the entire menu and the price of each item

for x in menu:
  print(f"{x} - {menu[x]:.2f}")




# TODO 2: Start a loop, asking the customer which item they would like to order

item = None
total = 0
while item != "Done":
  item = input("please state what you would like to order: ")
  if item in menu.keys():
    order.append({str(item):menu[item]})
    #order += {str(item):menu[item]}
    total += menu[item]


    # TODO 3: If the customer types a word check whether the requested item exists

    # TODO 4: Add valid items to the customer's order and let the loop continue

    # TODO 5: if the customer types "Done", end the loop and move to end of order


# TODO 6: Print out an itemized receipt for the user showing item and cost

# TODO 7: Print out the subtotal of the entire order

# for x in order:
#   print(f"{x}")

# print(f"Total: ${total:.2f}")


orders = ""
for x in order:
  for k in x:
    orders += f"{k} - {x[k]}\n\t"

summary = f"""
Order: {orders}
        Total: ${total}

"""

print(summary)



#print(f"""Order: {order} 
 #     Total: ${total:.2f}""")



# EXPECTED OUTPUT
# Order: Burger - 12.00
#        Fries  -  5.00
#        Drink  -  3.00
#         TOTAL: $20.00
