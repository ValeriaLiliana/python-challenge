import os
import csv


#define paths for the data
input_file="PyPoll/Resources/election_data.csv"
output_file = "PyPoll/analysis/election_results.txt"


#define varibales
total_votes=0
candidates = {}
winner = ""
winner_votes = 0


#open csv and create the loop
with open(input_file,newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    header = next(csvreader) #skip the header row

    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate]=1
    

#calculate precentages
candidate_percentage = {candidate: (votes/total_votes)*100 for candidate, votes in candidates.items()}

#calculate the winner
for candidate, votes in candidates.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

#print to terminal
print("Elections Results\n")
print("--------------------\n")
print(f"Total Votes: {total_votes}\n")
print("-----------------------\n")
for candidate, votes in candidates.items():
    percentage = candidate_percentage[candidate]
    print(f"{candidate}:{percentage:.3f}% ({votes})")

print("--------------\n")
print(f"Winner:{winner}")
print("--------------")


#add everything to a txt file
with open(output_file,"w") as txtfile:
    txtfile.write("Elections Results\n")
    txtfile.write("--------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-----------------------\n")

    #recalculate the same candiate stats from above and print to txt file
    #calculate all the candidate stats
    for candidate, votes in candidates.items():
     percentage = candidate_percentage[candidate]
     txtfile.write(f"{candidate}:{percentage:.3f}% ({votes})")


    txtfile.write("--------------\n")
    txtfile.write(f"Winner:{winner}\n")
    txtfile.write("--------------\n")


print("Complete")