import csv

csvpath = "Resources/budget_data.csv"

with open(csvpath) as budget_data:

    csvreader = csv.reader(budget_data, delimiter=",")
    
    month = []
    prof_loss = []
    total_prof_loss = 0

    for row in csvreader:
    
        date = row[0]

        mydate = date.split("-")
        
        month.append(mydate[0])

        prof_loss.append(row[1])

    prof_loss.remove('Profit/Losses')

    for a in range(0, len(prof_loss)): 
        prof_loss[a] = int(prof_loss[a]) 

    for b in range(0, len(prof_loss)): 
         total_prof_loss = total_prof_loss + prof_loss[b] 

    calc_prof_loss = [] 
  
    for c in range(1, len(prof_loss)): 
        calc_prof_loss.append(prof_loss[c] - prof_loss[c-1]) 
    
        average = sum(calc_prof_loss) / len(prof_loss)

        formatted_average = "${:,.2f}".format(average)

    total_months = len(month)


    print("Financial Analysis")
    print("---------------------------------------------------------")
    print(f"Total Months: {total_months - 1}")
    print(f"Total: ${total_prof_loss}")
    print(f"Average Change: {formatted_average}")
    print(f"Greatest Increase in Profits: ")
    print(f"Greatest Decrease in Profits: ")