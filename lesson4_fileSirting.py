"""
This program testing sorting and counting files according to extensions
"""
import unittest
import os
import shutil
import sortingops

directory = "v:\\workspace\\FileHandling_Homework\\fileSortingDirectory\\"

class TestSortingFiles(unittest.TestCase):
    """Test case to verify sorting files capabilities."""
    
    def setUp(self):
        os.mkdir(directory)
        self.path = directory
        os.chdir(self.path)
        self.file_names = ["file.txt", "file.sh", "file.exe", "file.cpp", "file1.txt", "file1.sh", "file1.exe"]
        for fn in self.file_names:
            f = open(self.path+fn, "w")
            f.close()
                     
    def test_sorting(self):
        os.chdir(self.path)
        sorted_dict = sortingops.sortingops()
        ext_testing = {'.cpp': 1, 
                       '.txt': 2,
                       '.sh': 2,
                       '.exe': 2                 
                       }
        
        self.assertEqual(ext_testing, sorted_dict, 'Both dicts must be equal')  
               
    def tearDown(self):
        #going back to src directory so it will be possible to remove fileSortingDirectory     
        os.chdir("v:\\workspace\\FileHandling_Homework\\src\\")    
        shutil.rmtree(directory)    
               
if __name__ == "__main__":
    unittest.main()
     
