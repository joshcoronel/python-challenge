import os
import csv


# Specify the file to read from
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pyroll_csv = os.path.join("Resources", "election_data.csv")

# Initilize variables
votes = 0
candidates = dict()
max = 0


# Open the file using "read" mode. Specify the variable to hold the contents
with open(pyroll_csv) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")

    # Skip header
    next(csvreader)

    for row in csvreader:
        votes = votes + 1
        if row[2] not in candidates:
            candidates[row[2]] = [1]
        else:
            candidates[row[2]][0] = candidates[row[2]][0] + 1
        
    for key in candidates.keys():

        candidates[key].append(candidates[key][0]/votes*100)
            
        if candidates[key][0]>max:
            max = candidates[key][0]
            winner = key


    print(votes)
    print(candidates)
    print(winner)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
output_file = os.path.join("analysis", "election_analysis.txt")

with open(output_file, 'w') as text:

    print("Election Results")
    text.write("Election Results\n")
    print("-------------------------")
    text.write("-------------------------\n")
    print(f'Total Votes: {votes}')
    text.write(f'Total Votes: {votes}\n')
    print("-------------------------")
    text.write("-------------------------\n")
    for key in candidates.keys():
        print(f'{key}: {candidates[key][1]:.3f} ({candidates[key][0]})')
        text.write(f'{key}: {candidates[key][1]:.3f} ({candidates[key][0]})\n')
    print("-------------------------")
    text.write("-------------------------\n")
    print(f'Winner: {winner}')
    text.write(f'Winner: {winner}\n')
    print("-------------------------")
    text.write("-------------------------")