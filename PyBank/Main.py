#In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
#Your task is to create a Python script that analyzes the records to calculate each of the following:

#import necessary modules
import os
import csv
## list relative path - directions to file from current file location
file_path = os.path.join("..", "Resources", "budget_data.csv")
