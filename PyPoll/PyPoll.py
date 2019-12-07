# PyPoll Homework 3

import os
import csv

# Create all required variables and data lists
votes = 0
candidates = []
khan = 0
correy = 0
li = 0
otooley = 0


# Files to load and output
csvpath = os.path.join("election_data.csv")
file_to_output = os.path.join("Poll_Data.txt")

# Open the CSV
with open(csvpath, newline="") as csvfile:
	# Store the contents in a CSV Reader
    csvreader = csv.reader(csvfile, delimiter=",")

    # Recognize header row
    csvheader = next(csvreader)

    for row in csvreader:
    	# Add a vote to the vote count
    	votes += 1

    	# Tally counts for each candidate

    	# First check if row is first occurance of candidate, if so append
    	# Gained inspiration for loop logic from GitHub user 'parismoscow', but modified extensively.
    	if row[2] not in candidates:
    		candidates.append(row[2])
    	# Collect count of individuals after captured in candidates
    	elif row[2] == "Khan":
    		khan += 1
    	elif row[2] == "Correy":
    		correy += 1
    	elif row[2] == "Li":
    		li += 1
    	elif row[2] == "O'Tooley":
    		otooley += 1

    # Find percentage of votes for each candidate
    khan_percent = (khan / votes) * 100
    khan_percent = round(khan_percent)
    khan_percent = "%.3f%%" % khan_percent
    correy_percent = (correy / votes) * 100
    correy_percent = round(correy_percent)
    correy_percent = "%.3f%%" % correy_percent
    li_percent = (li / votes) * 100
    li_percent = round(li_percent)
    li_percent = "%.3f%%" % li_percent
    otooley_percent = (otooley / votes) * 100
    otooley_percent = round(otooley_percent)
    otooley_percent = "%.3f%%" % otooley_percent

    # Find winner
    candidate_count = {khan : "Khan", correy : "Correy", li : "Li", otooley : "O'Tooley"}
    winner = candidate_count.get(max(candidate_count))

# Generate Poll Analysis Output
# Based on priciples from pyparagraph example
output_data = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {votes}\n"
    f"-------------------------\n"
    f"Khan: {khan_percent}\n"
    f"Correy: {correy_percent}\n"
    f"Li: {li_percent}\n"
    f"O'Tooley: {otooley_percent}\n"
    f"-------------------------\n"
    f"Winner: {winner}"
    )

print(output_data)

# Save the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_data)
