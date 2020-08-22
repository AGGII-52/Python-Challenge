#import necessary modules
import os
import csv

# list relative path
csvpath = os.path.join("..","Resources", "budget_data.csv")
output_path = os.path.join("..", "Analysis", "Results.txt")

#set variables
Total_Months = 0
Net_Total_PL = 0
Avg_Change = 0
Greatest_Increase_PL = 0
Greatest_Decrease_PL = 0

#read into file
with open(csvpath, "r") as csvfile:
    
    # preserve csv structure
    csvreader = csv.reader(csvfile, delimiter = ",")

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

      # Read each row of data after the header
    for row in csvreader:
        print(row)

    #skip header
    header = next(csvreader)
    #store list as variable
    contents = []

    #analyze data
    for row in csvreader:
        Total_Months += 1
        
        contents.append(row[1])
        PL = []
        Net_Total_PL = sum(PL)

        Avg_Change = Net_Total_PL / (len(PL))

        



#write into file
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------------------\n")
    txtfile.write(f"Total Months: {Total_Months}\n")
    txtfile.write("Net Total-Profits/Losses:\n")
    txtfile.write("Avg Change-Profits/Losses:\n")
    txtfile.write("Greatest Increase-Profits:\n")
    txtfile.write("Greatest Decrease-Profits:\n")
    
#print(Analysis)