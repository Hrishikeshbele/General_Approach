'''
delete folders containing less than 100 files.
'''
import os
import shutil

directory = r'/Users/varma/Downloads/lfw_funneled/'

for subfolder in os.listdir(directory):
    #we are only deleting folders not files so below line will check if it is folder
    if os.path.isdir(directory+subfolder): 
    	# print(subfolder)
    	# cal number of files in a folder
    	l =len(os.listdir(directory+subfolder)) 
    	if l < 100:
    		# Delete directory/folder
    		shutil.rmtree(directory+subfolder)
    	else:
    		print(subfolder + str(l))
