#PyPoll


import os, csv

#election_path = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')
file = r"C:\Users\alice\Downloads\python-challenge\Starter_Code\PyPoll\Resources\election_data.csv"

#initializing candidate list
candidate_list = []

#open csv
with open(file) as election:
    reader = csv.reader(election, delimiter= ",")
    header = next(reader)

    candidate_list = [candidate[2] for candidate in reader]
#total votes
total_votes = len(candidate_list)

#Get unique candidates
unique = []
for i in candidate_list:
    if i not in unique:
        unique.append(i)
#print(unique)

#vote counts for each candidate
vote_counts = [int(candidate_list.count(unique[0])),int(candidate_list.count(unique[1])), int(candidate_list.count(unique[2]))]

#combine two lists to make a dict
candidate_dict = dict(zip(unique, vote_counts))

#using dict, find winner
winner = max(candidate_dict, key = candidate_dict.get)

#print to terminal
print('Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'{unique[0]}: {vote_counts[0]/total_votes:.3%} ({vote_counts[0]})')
print(f'{unique[1]}: {vote_counts[1]/total_votes:.3%} ({vote_counts[1]})')
print(f'{unique[2]}: {vote_counts[2]/total_votes:.3%} ({vote_counts[2]})')
print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')

#txt file 
txt_file = r"C:\Users\alice\Downloads\python-challenge\Starter_Code\PyPoll\Resources\PyPoll_output.txt"
with open(txt_file, 'w') as text_file:
    print(f'Election Results', file = text_file)
    print(f'-------------------------', file = text_file)
    print(f'Total Votes: {total_votes}', file = text_file)
    print(f'-------------------------', file = text_file)
    print(f'{unique[0]}: {vote_counts[0]/total_votes:.3%} ({vote_counts[0]})', file = text_file)
    print(f'{unique[1]}: {vote_counts[1]/total_votes:.3%} ({vote_counts[1]})', file = text_file)
    print(f'{unique[2]}: {vote_counts[2]/total_votes:.3%} ({vote_counts[2]})', file = text_file)
    print(f'-------------------------', file = text_file)
    print(f'Winner: {winner}', file = text_file)
    print(f'-------------------------', file = text_file)
