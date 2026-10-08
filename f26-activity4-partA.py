# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 4
# Author Name: 
# Date: 

# SCENARIO
# You are wanting to save money for a particular purchase.
# Write a program that estimates how long it will take to grow your money to your desired amount.
# Consider 


# TODO 1: Create inputs for the following information 
#         - Your desired savings goal
goal = float(input("Enter your desired saving goal: "))
#         - The amount of money as your base investment
base = float(input("Enter your base investment: "))
#         - The annual interest rate
rate = float(input("Enter the annual interest rate: "))/12
#         - The amount of money you want to deposit into the account every month (if any)
deposit = float(input("Enter the deposit amount: "))

# TODO 2: Create variables to hold number of months and current balance of the account

months = 0
balance = base

# TODO 3: Create a loop that will run until you have made at least your desired savings goal

while balance < goal:
  #balance += (balance + deposit) * rate

    # TODO 4: Calculate amount of money earned that month through interest on your base investment and monthly deposit
    monthly_earning = (balance * rate)
    balance += monthly_earning + deposit
  

    # TODO 5: Increment the number of times the loop has run so you can track how many months it takes to hit your goal
    months += 1

# TODO 6:  Print how long it will take for your investment to mature.  
#          If the duration is longer than 12 months, print your result in years.  Otherwise, print the result in months.

years = ""
if months > 12:
  years = f"Number of Years: {months/12:.2f}"

summary =f"""
Goal: ${goal}
Interest: {rate*12}%
Base: ${base}
Monthly Deposit: ${deposit}


Number of Months: {months} 
{years}
Total Investment: ${balance:.2f}

"""

print(summary)


# EXPECTED OUTPUT
# GOAL: $1,000,000
# INTEREST: 4%
# BASE: $1,000
# MONTHLY DEPOSIT: $100
#
# Number of Months: 177
# Number of Years: 87.75
# Total Investment: $1,034,906.36

