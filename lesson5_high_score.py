"""
This function takes two arguments, a string player name and an integer score, 
and keeps a "high score" table in a Python shelve.
"""

import shelve

def high_score(name, score):
    
    shelf = shelve.open('high_score.shlf')
    
    if name in shelf:
        #getting by name actual high score from the shelf
        high_score = shelf.get(name)
        if score > high_score:
            shelf[name] = score
        else:
            shelf[name] = high_score
    else:
        shelf[name] = score
            
    high_score = shelf.get(name)        
    shelf.close()
    return high_score
