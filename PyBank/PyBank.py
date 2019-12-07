# PyBank Homework 3

import os
import csv

# Create all required data lists
months = []
profit = []
month_change = []

# Files to load and output
csvpath = os.path.join("budget_data.csv")
file_to_output = os.path.join("Bank_Data.txt")

# Open the CSV
with open(csvpath, newline="") as csvfile:
	# Store the contents in a CSV Reader
    csvreader = csv.reader(csvfile, delimiter=",")

    # Recognize header row
    csvheader = next(csvreader)

    # For loop to gain values of each row
    for row in csvreader:

    	# Append months to keep track of dates
    	months.append(row[0])
    	# Append profit to keep track of profits
    	profit.append(int(row[1]))

    # For loop to find change in profits month-to-month (length - 1, to make i + 1 math work below)
    # Gained inspiration for loop logic from GitHub user 'cantugabriela', modified for simplification of output of data
    for i in range(len(profit) - 1):

    	# Find the difference between two months, append to monthly change
    	month_change.append(profit[i + 1] - profit[i])

# Find the greatest month change.
great_increase_profit = max(month_change)
great_decrease_profit = min(month_change)

# Index the max increase and decrease months by looking for the month following the max and min in month_change
great_increase_month = month_change.index(max(month_change)) + 1
great_decrease_month = month_change.index(min(month_change)) + 1 

# Generate Bank Analysis Output
# Based on priciples from pyparagraph example
output_data = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {len(months)}\n"
    f"Total: ${sum(profit)}\n"
    f"Average Change: ${round(sum(month_change)/len(month_change),2)}\n"
    f"Greatest Increase in Profits: {months[great_increase_month]} (${(str(great_increase_profit))})\n"
    f"Greatest Decrease in Profits: {months[great_decrease_month]} (${(str(great_decrease_profit))})"
    )

print(output_data)

# Save the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_data)
