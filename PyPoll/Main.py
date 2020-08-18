#import necessary modules
import os
import csv
## list relative path - directions to file from current file location
file_path = os.path.join("..", "Resources", "election_data.csv")
##read into file, or write into file
with open(file_path, "r") as csvfile:
 # preserve csv structure
    csvreader = csv.reader(csvfile, delimiter = ",")
    #preview data - skip header
    header = next(csvreader)
    #store list as variable
    contents = []

    for row in csvreader:
        contents.append(row)
