import unittest, zip_dir, os, shutil

class TestZip(unittest.TestCase):
                
    def setUp(self):
        self.path = r"v:\workspace\Archives_Homework\src\zip_test"
        os.mkdir(self.path)
        self.file_names = ["file1", "file2", "file3"]
        for fn in self.file_names:
            f = open(os.path.join(self.path, fn), "w")
            f.close()

    def test_zip(self):
        
        print(os.getcwd())
        expected = [ "zip_test/" + fn for fn in self.file_names ]
        observed = zip_dir.zip_dir(self.path) # this is what we get from function
        print(expected)
        print(observed)
        self.assertEqual(expected, observed)
        self.assertEqual(set(expected), set(observed))
        
    def tearDown(self):
        
        try:
            shutil.rmtree(self.path, ignore_errors=True)
        except IOError:
            pass

if __name__ == "__main__":
    unittest.main()
