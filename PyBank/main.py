import os
import csv


# Specify the file to read from
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pybank_csv = os.path.join("Resources", "budget_data.csv")

# Initilize variables
net = 0
months = 0
date = []
profitloss = []


# Open the file using "read" mode. Specify the variable to hold the contents
with open(pybank_csv) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")

    # Skip header
    next(csvfile)

    # Calculate the net value of profit/loses and count number of months
    for row in csvreader:
        net = net + round(float(row[1]))
        months = months + 1 
        date.append(row[0])
        profitloss.append(float(row[1]))


    
    # Use the net value and total number of months to calculate the average change
    avg_change = round(net/months,2)

    maxVal = max(profitloss)
    maxInd = profitloss.index(maxVal)
    maxDate = date[maxInd]

    minVal = min(profitloss)
    minInd = profitloss.index(minVal)
    minDate = date[minInd]

output_file = os.path.join("analysis", "budget_analysis.txt")
with open(output_file,'w') as text:

    print("Financial Analysis")
    text.write("Financial Analysis \n")
    print("----------------------------")
    text.write("----------------------------\n")
    print(f'Total Months: {months}')
    text.write(f'Total Months: {months}\n')
    print(f'Total: ${net}')
    text.write(f'Total: ${net}\n')
    print(f'Average Change: ${avg_change}')
    text.write(f'Average Change: ${avg_change}\n')
    print(f'Greatest Increase in Profits: {maxDate} (${maxVal})')
    text.write(f'Greatest Increase in Profits: {maxDate} (${maxVal})\n')
    print(f'Greatest Decrease in Profits: {minDate} (${minVal})')
    text.write(f'Greatest Decrease in Profits: {minDate} (${minVal})\n')

    
    
