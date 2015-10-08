"""
This program checks the content of passed directory and 
count of how many files have each extension (".txt", ".doc", etc.)
"""
import os

def sortingops():
    directory = os.getcwd()
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    extensions = {}
    for file in files:
        fileName, fileExtension = os.path.splitext(file)
        if fileExtension in extensions:
            extensions[fileExtension] += 1
        else:
            extensions[fileExtension] = 1
            
    for key, value in extensions.items():
        print(key, value) 
    return extensions             
