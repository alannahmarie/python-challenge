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

    for row in csvreader:

        total_votes = total_votes + 1 

        candidates = row[2]
        
        # if row[2] == "Khan":

        #     khan_votes = (int(row[0])) + 1

        # if row[2] == "Correy":
        #     correy_votes = (int(row[0])) + 1

        # if row[2] == "Li":
        #     li_votes = (int(row[0])) + 1

    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------------")
    print(f"Khan: ({khan_votes})")
    # print(f"Correy: ({correy_votes})")