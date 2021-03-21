#  The data we need to retreive.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. Th winner of the election based on popular vote.

#Add dependencies
import csv
import os
# Assign a variable for the file to load from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1 Initialize a total vote counter
total_votes = 0

#Initialize list for candidates
candidate_options = []

#Initialize dictionary for vote counts
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    #To Do: Read and Analyze Data
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    #Print headers in the CSV.
    headers = next(file_reader)
    print(headers)
    
    #Print each row in CSV.
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1
        
        #Print the candidate name form each row
        candidate_name = row[2]

        #add the candidate name to candidate list if unique
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            #Begin vote count for each candidate
            candidate_votes[candidate_name] = 0

        #Add a vote to candidate's count
        candidate_votes[candidate_name] += 1

#Save the results to our text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
        #Determine percentage of votes for each candidate by looping through counts
        # 1 Iterate through candidate list
    for candidate_name in candidate_votes:
        # 2 Retrieve vote count of candidate
        votes = candidate_votes[candidate_name]
        # 3 Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4 Print candidate name and percentage of votes
        
        #Compare candidates with winning numbers. If candidate is in lead set as winning.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)