  # Programmers: Oreoluwa Adebusoye, Cameron Combariza
  # Course:  CS151, Dr. Zelalem Jembre Yalew
  # Due Date: 9/18/2024
  # Lab Assignment: 1
  # Problem Statement: This program calculates the total cost of gas for the trip based on
  #                    Total miles to be traveled (miles), Vehicle's fuel efficiency in miles per gallon (MPG)
  #                    and Cost of gas per gallon
  # Data In: 1. Total Miles for the Trip:
  #          2. Vehicle's MPG (Miles Per Gallon):
  #          3. Cost of Gas per Gallon
  # Data Out:  1. Total Cost of Gas
  #            2. Formatted Output Message
  # Credits: This code is based on the techniques we have learnt in class

# Programme:

# Prompt the user to enter the total miles for the trip
total_miles = float(input("Enter the total miles for the trip: "))
print ("")

# Prompt the user to enter the MPG of their vehicle.
miles_per_gallon = float(input("Enter the vehicle's MPG: "))
print ("")

# Prompt the user to enter the cost of gas per gallon
price_per_gallon = float(input("Enter the cost of gas per gallon: "))
print ("")

# Calculate total gas cost of trip
total_cost = total_miles / miles_per_gallon * price_per_gallon

# Output the Result
print(f"The total cost of gas for your trip is: ${total_cost:.2f}")
