# Import csv module and read csv file
import csv

csvpath = "/Users/alannahmarie/Desktop/python-challenge/PyBank/Resources/budget_data.csv"

with open(csvpath) as budget_data:

    csvreader = csv.reader(budget_data, delimiter=",")

    # Remover header from iterable data
    next(csvreader)

    # Define variables that you will use in for looo
    total_months = 0
    profit_losses = 0
    average_change = 0 
    increase = 0
    decrease = 0 
    prev_row = 0 
    next_row = prev_row + 1
    # Create a for loop that will iterate over all rows of data
    for row in csvreader:

        total_months = total_months + 1
        profit_losses = profit_losses + (int(row[1]))
       

print("Financial Valuation")
print("----------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${profit_losses}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: $ {increase}")
print(f"Greatest Decrease in Profits: $")