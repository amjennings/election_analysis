#import dependencies
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save teh file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initilize a total vote counter
total_votes = 0
#Candidate options
candidate_options = []
#Declare the empty dictionary
candidate_votes = {}
#Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read the header row.
    headers = next(file_reader)
    #Print each row in CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1
        #Get the candidate name from each row.
        candidate_name = row[2]
        #If the candidate name does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add candidate name to the candidate list
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
#Save the results to our text file
with open(file_to_save, "w") as txt_file:
    #After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n")
    print(election_results, end="")
    #After printing the final vote count to the terminal save the final
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #Print the candidate's name, vote count, and percentage of votes to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file
        txt_file.write(candidate_results)

        #Determine winning vote count, winning percentage, and winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percentage = vote_perecentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    #Print the winning candidate's resutls to the terminal.
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")
    print(winning_candidate_summary)
    #Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
