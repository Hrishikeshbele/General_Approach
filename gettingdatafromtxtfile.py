'''
given a txt file with each row containing some no of words. we have to take out each column from it containg entries of perticular index 
in a row.
'''

ex. file containing 2 entries in each row

#since there are two columns in txt file we split each line and store first and second in diff list's
col1,col2 = [], []
with open(r'features.txt', 'r') as f:
    for line in f:
        first, second = line.split()
        col1.append(first)
        col2.append(second)
