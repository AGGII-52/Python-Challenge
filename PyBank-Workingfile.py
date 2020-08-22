#import necessary modules
import os
import csv

# list relative path
csvpath = os.path.join( 'Resources', 'budget_data.csv')
out_path = os.path.join( 'Analysis', 'Results.txt')

list = []
listMonths = []
listProfit_Loss = []

#read into file
with open(csvpath, 'r') as csvfile:
    
    #preserve csv structure
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    print(csvreader)
    
     # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

    #skip header
    #header = next(mainlist)
    
    #store list as variable
    #list = []

    #print(list)