'''
problem:
given a folder containing around 200 folders and each of 200 folder contains csv files in folder named csvfloder .we have to delete
first 2000 columns of each csv file 
my approach:
iterate through different folders using different path each time modify path during each iteration using os.path.join and read csv files 
in it then create dataframe of each csv file and then perform operations of dataframe to create new dataframe and then save 
new dataframe to new csv file
'''
#code for deleting first 2000 columns from csv files automatically interate through different folders
import os
import pandas as pd
import glob
path1 =r'C:\Users\hrishi bele\Downloads\files'
#get list of all folders through which we want to iterate
folder_names=os.listdir(r'C:\Users\hrishi bele\Downloads\files')
for names in folder_names:
    #joining path for each iteration
    pathc=os.path.join(path1,names,'csvfloder')
    files=os.listdir(pathc)
    #will fetch list of files ending with .csv in given directory
    all_files = glob.glob(pathc + "/*.csv")
    for filename in all_files:
        if filename.endswith(".csv"):
            df=pd.read_csv(filename)
            df1=df.iloc[:,2000:]
            print("now deleting columns from:",filename)
            df1.to_csv(filename+'.csv', index=False)
            continue
        else:
            continue
