#import dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save teh file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:
    #print the file object
    print(election_data)

    # to do: read and analyze the data here
    file_reader = csv.reader(election_data)

    #Print each row in the CSV file.
    for row in file_reader: 
        print(row)
