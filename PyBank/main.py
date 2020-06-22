import os
import csv


# Specify the file to read from
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pybank_csv = os.path.join("Resources", "budget_data.csv")

# Initilize variable. These variables actually won't be arrays, but I will keep here for know until I write the code
total_months = []
net = []
avg_change = []
max_profit = []
max_loss = []

# Open the file using "read" mode. Specify the variable to hold the contents
with open(pybank_csv) as csvfile

    csvreader = csv.reader(csvfile,delimiter=",")

    for row in csvreader:
        
