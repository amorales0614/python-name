#import dependencies
import os
import csv

#read in csv file
pollpath = os.path.join("Resources","election_data.csv")

#set variables and lists
voteCount = 0
candidateVotes = []
candidateCount = []
uniqueCandidates = []
percent = []

#open the csv file and skip header
with open(pollpath) as pollfile:
	pollreader = csv.reader(pollfile, delimiter=",")
	poll_header = next(pollreader)

	#initiate for loop
	for row in pollreader:

		#count votes by just counting rows
		voteCount = voteCount + 1

		#identify unique candidates and add to list for later
		if row[2] not in uniqueCandidates:
			uniqueCandidates.append(row[2])

		#add votes to candidateVotes list
		candidateVotes.append(row[2])

	#second loop to populate candidate counts
	for x in uniqueCandidates:
		candidateCount.append(candidateVotes.count(x))
		percent.append(round(candidateVotes.count(x)/voteCount*100,3))

	#identifying winner
	winner = uniqueCandidates[candidateCount.index(max(candidateCount))]

	#printing results
	print("---------------------")
	print("Election Results")
	print("---------------------")
	print("Total Votes: " + str(voteCount))
	print("---------------------")
	for a in range(len(uniqueCandidates)):
		print(f'{uniqueCandidates[a]}: {percent[a]}% {candidateCount[a]}')
	print("---------------------")
	print("Winner: " + winner)
	print("---------------------")

	#export to text file
	with open('electionanalysis.txt', 'w') as text:
		text.write("----------------------\n")
		text.write("Election Results\n")
		text.write("----------------------\n")
		text.write("Total Votes: " + str(voteCount) + "\n")
		text.write("----------------------\n")
		for a in range(len(uniqueCandidates)):
			text.write(f'{uniqueCandidates[a]}: {percent[a]}% {candidateCount[a]}\n')
		text.write("----------------------\n")
		text.write("Winner: " + winner + "\n")
		text.write("----------------------\n")


