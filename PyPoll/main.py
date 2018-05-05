# Alex Schackmuth
# hw3 python
# PyPoll

### Import dependencies
import os
import csv
from collections import Counter

### File paths
csvpath = os.path.join("raw_data", "election_data_1.csv")
output_file = os.path.join("election_results.txt")

### Read election data csv and count results
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    lines = [line for line in csvreader]
    votes = list(Counter([l[2] for l in lines]).items())

### Find total votes
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    total_votes = sum(1 for row in csvreader)
    votes.append(('Total Votes', total_votes))

### Creating the rows for the output file
names = [i[0] for i in votes]
vote_count = [i[1] for i in votes]
vote_percent1 = [x*100 for x in[x/total_votes for x in vote_count]]
vote_percent = [ '%.2f' % elem for elem in vote_percent1 ]
y = 0
while vote_count[y+1] > vote_count[y]: 
    y = y+1
winner = names[y]

### print results
print("-"*40)
print("Total Votes " + str(total_votes))
print("-"*40)
for z in range(len(names)): 
    print(names[z] + ": " + str(vote_percent[z]) + "% " + str(vote_count[z])) 
print("-"*40)
print("Winner:" + winner)
print("-"*40)

### create txt file with results
f = open(output_file,'w')
f.write("-"*40)
f.write("\n")
f.write("Total Votes " + str(total_votes))
f.write("\n")
f.write("-"*40)
f.write("\n")
for z in range(len(names)): 
    f.write(names[z] + ": " + str(vote_percent[z]) + "% " + str(vote_count[z]))
    f.write("\n")
f.write("-"*40)
f.write("\n")
f.write("Winner:" + winner)
f.write("\n")
f.write("-"*40)
f.write("\n")
f.close()

