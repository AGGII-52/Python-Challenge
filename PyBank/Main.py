#import necessary modules
import os
import csv

# list relative path
input_path = os.path.join( "Resources", "budget_data.csv")
output_path = os.path.join( "Analysis", "Results.txt")
#set variables
Total Months = 0
Net Total-Profits/Losses = 0
Avg Change = 0
Greatest Increase-Profis/Losses = 0
Greatest Decrease-Profits/Losses = 0
#read into file
with open(input_path, "r") as csvfile:
    
    # preserve csv structure
    csvreader = csv.reader(csvfile, delimiter = ",")
    #skip header
    header = next(csvreader)
    #store list as variable
    contents = []

    #analyze data
    for row in csvreader:
        contents.append(row[0])

#write into file
with open(output_path, "w") as txtfile:
    txtfile.writer("Financial Analysis")
    txtfile.writer("---------------------------")
    txtfile.writer("Total Months")
    txtfile.writer("Net Total-Profits/Losses")
    txtfile.writer("Avg Change-Profits/Losses")
    txtfile.writer("Greatest Increase-Profits")
    txtfile.writer("Greatest Decrease-Profits")
    
print(contents)

