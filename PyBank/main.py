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
    change = 0 

    average_change = 0

    month = []
    money = []
    
    # Create a for loop that will iterate over all rows of data
    for row in csvreader:

        money.append(int(row[1]))
        month.append(row[0])

        total_months = total_months + 1
        profit_losses = sum(money)
    
        increase = max(money)
        decrease = min(money)

        max_index = money.index(increase)
        min_index = money.index(decrease)
        
        

    change = money[-1] - money[0]
    average_change = round((change) / (total_months -1), 2)


print(" ")
print("Financial Valuation")
print("----------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${profit_losses}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {month[max_index]} (${money[max_index]})")
print(f"Greatest Decrease in Profits: {month[min_index]} (${money[min_index]})")

output_path = "/Users/alannahmarie/Desktop/python-challenge/PyBank/Analysis/analysis.txt"

with open(output_path, 'w', newline='') as txt:
    txt.write(" \n")
    txt.write('Financial Valuation\n') 
    txt.write('----------------------------------------------------\n') 
    txt.write(f"Total Months: {total_months}\n") 
    txt.write(f"Total: ${profit_losses}") 
    txt.write(f"Average Change: ${average_change}\n") 
    txt.write(f"Greatest Increase in Profits: {month[max_index]} (${money[max_index]})\n") 
    txt.write(f"Greatest Decrease in Profits: {month[min_index]} (${money[min_index]})") 
