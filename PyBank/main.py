import os
import csv


# Specify the file to read from
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pybank_csv = os.path.join("Resources", "budget_data.csv")

# Initilize variables
net = 0
months = 0
monthly_change = 0
total_change = 0
maxChange = -99999
minChange = 99999


# Open the file using "read" mode. Specify the variable to hold the contents
with open(pybank_csv) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")

    # Skip header
    next(csvfile)

    # Calculate the net value of profit/loses and count number of months
    for row in csvreader:
        net = net + round(int(row[1]))
        months = months + 1 
        
        if months > 1:
            monthly_change = int(row[1]) - previous_row
            total_change = total_change + monthly_change
        
        previous_row = int(row[1])

        if monthly_change > maxChange:
            maxChange = monthly_change
            maxMonth = row[0]

        if monthly_change < minChange:
            minChange = monthly_change
            minMonth = row[0]
    
    # Use the net value and total number of months to calculate the average change
    avg_change = round(total_change/(months-1),2)

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
    print(f'Greatest Increase in Profits: {maxMonth} (${maxChange})')
    text.write(f'Greatest Increase in Profits: {maxMonth} (${maxChange})\n')
    print(f'Greatest Decrease in Profits: {minMonth} (${minChange})')
    text.write(f'Greatest Decrease in Profits: {minMonth} (${minChange})\n')

    
    
