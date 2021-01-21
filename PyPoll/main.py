import csv

csvpath = "/Users/alannahmarie/Desktop/python-challenge/PyPoll/Resources/election_data.csv"

with open(csvpath) as election_data:

    csvreader = csv.reader(election_data, delimiter=",")

    # Remover header from iterable data
    next(csvreader)

    total_votes = 0
   
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0 
  
    names = []
    candidates = []

    for row in csvreader:
        
        total_votes = total_votes + 1 

        names = row[2]

        if row[2] not in candidates:
            candidates.append(row[2])

        for i in names:
            if i not in names:
                candidates.append(i)

        if names == "Khan":
            khan_votes = khan_votes + 1
        elif names == "Correy":
           correy_votes = correy_votes + 1
        elif names == "Li":
            li_votes = li_votes + 1
        else:
            otooley_votes = otooley_votes + 1

        percent_khan = (khan_votes / total_votes * 100)
        percent_correy = (correy_votes / total_votes * 100)
        percent_li = (li_votes / total_votes * 100)
        percent_otooley = (otooley_votes / total_votes * 100)

    determine_winner = [khan_votes, correy_votes, li_votes, otooley_votes]

    winner = (max(determine_winner))


print(" ")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{candidates[0]}: {(format(percent_khan, '.3f'))}% ({khan_votes})")
print(f"{candidates[1]}: {(format(percent_correy, '.3f'))}% ({correy_votes})")
print(f"{candidates[2]}: {(format(percent_li, '.3f'))}% ({li_votes})")
print(f"{candidates[3]}: {(format(percent_otooley, '.3f'))}% ({otooley_votes})")
print("--------------------------")
print(f"Winner: {candidates[0]}")
print("--------------------------")

output_path = "/Users/alannahmarie/Desktop/python-challenge/PyPoll/Analysis/analysis.txt"

with open(output_path, 'w', newline='') as txt:
    txt.write(" \n")
    txt.write("Election Results\n")
    txt.write("-------------------------\n")
    txt.write(f"Total Votes: {total_votes}\n")
    txt.write("-------------------------\n")
    txt.write(f"{candidates[0]}: {(format(percent_khan, '.3f'))}% ({khan_votes})\n")
    txt.write(f"{candidates[1]}: {(format(percent_correy, '.3f'))}% ({correy_votes})\n")
    txt.write(f"{candidates[2]}: {(format(percent_li, '.3f'))}% ({li_votes})\n")
    txt.write(f"{candidates[3]}: {(format(percent_otooley, '.3f'))}% ({otooley_votes})\n")
    txt.write("--------------------------\n")
    txt.write(f"Winner: {candidates[0]}\n")
    txt.write("--------------------------")