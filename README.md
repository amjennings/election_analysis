# election_analysis

## Project Overview
This project was requested by a Colorado Board of Elections employee. This project contains an election audit of a recent local congressional election. The following information is included:

1. The total number of votes.
2. The percentage of votes and total number of votes from each county. 
4. The county with the largest turnout.
5. The percentage of votes and total number of votes each candidate received. 
6. The winner of the election based on popular vote.

## Resources
-Data Source: election_results.csv
-Software: Python 3.9.5, Visual Studio Code 1.64.0

## Election Audit Results
The analysis of the election shows: 
-There were 367,711 votes cast in the election.

- Below is the voter turnout by county:

  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)  

- The county with the largest voter turnout was Denver.

- The candidate results were: 

  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
  
- The following code was used to calculate the total votes for each candidate:
```
      if candidate_name not in candidate_options:
           candidate_options.append(candidate_name)
           candidate_votes[candidate_name] = 0
      candidate_votes[candidate_name] += 1
```
- The winner of the election was: 

  - Diana DeGette, who received 73.8% of the vote and 272,892 votes.

- This code produced this same information above as a printed summary and in a text file as shown here. 
![election_results](https://user-images.githubusercontent.com/98051208/154706110-84a4a29e-a6d0-4d9c-a802-dd8b622d2e0b.png)


## Election Audit Summary
The code from this election audit could be used for other elections. One way this could be done, would be simply uploading a different CSV file with election results from another year or region of Colorado. This new file should have the same format as the current file containing the ballot ID, county, and candidate. If this file had a different name (e.g., "election_results_2020") there is only one line of code that would need to be adjusted. Alternatively, if the file name were the same, the results could be differentiated by adjusting the printed summaries to specify the details of the results. For example, currenlty the summaries print statements including, "Total Votes: 369,711" and "Largest County Turnout: Denver" for example. These summaries could be adjusted to state "Total Votes in 2019: 369,711" and "Largest County Turnout in 2019: Denver".
