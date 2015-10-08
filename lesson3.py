"""
The tests do not actually test anything - this is a demo.
"""
import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
    
    def test_1(self):
        lst1 = []
        lst2 = []
        "Verify creation of files is possible"
        for filename in ("this.txt", "that.txt", "the_other.txt"):
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
            #creating a list of files created by for loop
            lst1.append(filename)
        #sorting by alphabetical order so it will be possible to compare    
        lst1.sort()    
        #creating a list of all files that are into the temp directory
        lst2 = os.listdir()
        lst2.sort()
        #print(lst1) #for debugging purpose
        #print(lst2) #for debugging purpose
        self.assertListEqual(lst1, lst2, "two lists must be the same")
        
    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")
        
    def test_3(self):
        f = open("binaryfile" , "wb") #'b' stands for binary
        "Creating 1M file"
        f.write(b'X' * 1000000) #'b' stands for binary
        f.close()
        statinfo = os.stat('binaryfile')
        #print(statinfo.st_size) #for debugging purpose
        self.assertEqual(1000000, statinfo.st_size, "two files must be the same size")
                

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)

if __name__ == "__main__":
    unittest.main()
