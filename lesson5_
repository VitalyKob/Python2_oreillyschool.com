"""
This program verifying highest_score function.
"""

import high_score
import unittest
import glob 
import os

class TestHighScore(unittest.TestCase):
    """Test case to verify high score."""
    
    def test_high_score(self):
        scores = [1,2,3,4,5,1,2,3,4]
        highest = max(scores)
        #feeding the function with scores from scores list at the end h_score must have highest score from the list
        for score in scores:
            h_score = high_score.high_score('Ronald', score)
        self.assertEqual(highest, h_score, 'Both scores must be equal')
        
    def testStoreHighScore(self):
        HighScore = high_score.high_score
        self.assertEqual(-100, HighScore('joe', -100))
        self.assertGreater(-99, HighScore('joe', -100))
        self.assertEqual(0, HighScore('joe', 0))
        self.assertLess(0, HighScore('chris', 100))
        self.assertEqual(1000, HighScore('chris', 1000))
        self.assertLess(100, HighScore('chris', 1000))
        self.assertEqual(0, HighScore('joe', -1))
       
    def test_many_scores(self):
        HighScore = high_score.high_score
        self.assertEqual(50, HighScore('Kirby', 50))
        self.assertEqual(150, HighScore('Kirby', 150))
        self.assertEqual(150, HighScore('Kirby', 40))
        self.assertEqual(150, HighScore('Kirby', 95))
        self.assertTrue(HighScore('Kirby', 180) == 180, 'Kirby should have 180 as a top score')     
        
    def tearDown(self):
        files = glob.glob('high_score.shlf.*')
        for f in files:        
            os.remove(f)
        
if __name__ == "__main__":
    unittest.main()
        
