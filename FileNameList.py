# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 21:45:21 2018
Function: Filename Sniffer
Description:  This function looks at all of the files in a given workspace, 
and outputs a dictionary containing lists of all of the files (as strings), 
sorted into the following categories:

    Key:     List of file names with extension:
    "text"        .txt
    "csv"         .csv
    "xlsx"        .xlsx
    "xls"         .xls
    "other"       any other file types 

example: 
    dict["txt"] --> ["file.txt", "another_file.txt", "etc"]
    
The function will also 'sniff' files 1 subfolder level down.

Example of function in use use:
    
    
    wksp = r"C:\path\to\folder"
    dict = {}
    
    dict = FileSniffer(wksp)
    print("\nFiles Dictionary:" + str(dict))
    print("\nKeys: " + str(dict.keys()))
    print("\nValues :" + str(dict.values()))
    print("\nItems: " + str(dict.items()))
    print("\nText Files: " + str(dict["txt"]))


@author: Liam
"""

import os

def FileSniffer(workspace):
    wksp = workspace
    # Change directory to match workspace
    os.chdir(wksp)
    
    cwd = os.getcwd()
    print("New Working Directory: " + cwd)
    
    # Create list of folders and files current directory
    dirLST = os.listdir('.')
        
    # Sort through files and create lists by file type
    
    ## create file type lists to contain sorted files
    txtLST = []
    csvLST = []
    xlsxLST = []
    xlsLST = []
    otherLST = []
    
    ## loop through files and add to file type lists
    for i in range(len(dirLST)):
        if ".txt" in dirLST[i]:
            txtLST.append(dirLST[i])
            
        elif ".csv" in dirLST[i]:
            csvLST.append(dirLST[i]) 
            
        elif ".xlsx" in dirLST[i]:
            xlsxLST.append(dirLST[i])
            
        elif ".xls" in dirLST[i]:
            xlsLST.append(dirLST[i])
            
        else: 
            otherLST.append(dirLST[i])

    # Create Master filename list Dictionary
    FilesDict = {}
    
    # Add lists by file type to Master Filenames Dictionary
    FilesDict["txt"]= txtLST
    FilesDict["csv"]= csvLST
    FilesDict["xlsx"]= xlsxLST
    FilesDict["xls"]= xlsLST
    FilesDict["other"]= otherLST
    return FilesDict

wksp = r"Q:\path\to\folder"
dict = {}

dict = FileSniffer(wksp)
print("\nKeys: " + str(dict.keys()))
print("\n\n")
print("\nValues :" + str(dict.values()))
print("\n\n")
print("\nItems: " + str(dict.items()))
print("\n\n")
print("\nText Files: " + str(dict["txt"]))
