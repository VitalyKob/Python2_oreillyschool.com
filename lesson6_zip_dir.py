"""

This function receiving a path to target directory and archiving the directory :
directory_name/file_name. The function archiving only files into target directory.

"""

import os, zipfile

def zip_dir(path):
    
    current_dir = os.getcwd()
    print(current_dir)
    files = os.listdir(path) #getting list of files from directory into path
    dirname = os.path.basename(path) #getting directory name which contains the files
    archive_fn = "my_archive.zip"
    zf = zipfile.ZipFile(archive_fn, "w")
    goup = os.path.dirname(path)
    os.chdir(goup) #go one level up
    for f in files:
        fn = os.path.join(dirname,os.path.relpath(f)) #construct directory_name/filename
        if os.path.isfile(fn): #checking if fn is file
            zf.write(fn)
    zf.close()
    os.chdir(current_dir) #go back to original directory
    return(zf.namelist())
