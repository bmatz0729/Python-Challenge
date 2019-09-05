import os
import csv




Mybank = os.path.join("election_data.csv")

with open(Mybank, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ",")

	csv_header = next(csvreader)

	
	runner = [] #candidate
	votes_cast = 0
	votes_counted = []
	winner = []
	total_votes = 0
	percentage = []


	first_row = next(csvreader)

	for row in csvreader:
		votes_cast = votes_cast + 1

		cand = row[2]


	if cand in runner:
		candidate_index = runner.index(cand)
		votes_counted[candidate_index] = votes_counted[candidate_index] + 1
	else:
		runner.append(cand)
		votes_counted.append(1)


max_counted = votes_counted[0]
max_index = 0
#find percentage of vote for each candidate and the winner
for count in range(len(runner)):
	vote_percentage = votes_counted[count]/votes_cast*100
	percentage.append(vote_percentage)
	if votes_counted[count] > max_counted:
		max_counted = votes_counted[count]
		print(max_votes)
		max_index = count
		winner = runner[max_index]


print(f"Total Votes: {votes_cast}")
print(f"Winner: {winner}")