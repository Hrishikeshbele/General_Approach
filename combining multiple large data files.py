#code to combine multiple files having large size 
import glob
import os
import csv
from more_itertools import unique_everseen
class Combine:
   def __init__(self,path):
       self.path= path
       os.chdir(self.path)
   def GetFileNames(self):
       return glob.glob('Final_*.csv')
   def Merge(self):
       Filenames= self.GetFileNames()
       #print(Filenames)
       for i in range(len(Filenames)):
           if i==0:#creating out file for the first time
               with open(Filenames[0], 'r') as infile, open('combined.csv', 'w',newline='') as outfile:
                   reader= csv.DictReader(infile)
                   fieldnames= reader.fieldnames
                   writer = csv.DictWriter(outfile,fieldnames=fieldnames)
                   writer.writeheader()
                   for row in reader:
                       writer.writerow(row)
           else:# appending on the created outfile
                 with open(Filenames[i], 'r') as infile, open('combined.csv', 'a',newline='') as outfile:
                   reader= csv.DictReader(infile)
                   writer = csv.DictWriter(outfile,fieldnames=fieldnames)
                   for row in reader:
                      writer.writerow(row)
       #removing duplicates and saving in different file.
       with open('combined.csv','r') as f, open('OutputFile.csv','w') as out_file:
           out_file.writelines(unique_everseen(f))
       os.remove('combined.csv')
      
ToCombine= Combine('H:\INTERN\Inventiff\data_files')
ToCombine.Merge()
