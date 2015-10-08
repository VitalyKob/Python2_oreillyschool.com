# Python2_oreillyschool.com
# Python2 

# Lesson2

Here are your instructions:


Make a UnitTesting_Homework project and assign it to the Python2_Homework working set. In this project, write a unittest test program for the following function. (The test program makes unittest.TestCase assertions about the results of calling the function with known arguments.)
def title(s):
    "How close is this function to str.title()?"
    return s[0].upper()+s[1:]
Test your results for a given string s by comparing them with s.title(). Because this is purely an exercise, it's OK to put your test code in the same file as the function and just hand in a single file. Your file should be an importable module. You should be able to find an example that shows title(s) and s.title() diverge (have different output). Bonus marks for fixing the error in the function above (making it behave more like the native method).


# Lesson3

Here are your instructions:


Make a TestDrivenDevelopment_Homework project and assign it to the Python2_Homework working set.

Copy the setupDemo.py file from the TestDrivenDevelopment/src folder to the TestDrivenDevelopment_Homework/src folder.

Modify it so that:
•The test_1() method includes code to verify that the test directory contains only the files created by the for loop. Hint: You might create a set containing the list of three filenames, and then create a set from the os.listdir() method.
•A test_3() method creates a binary file that contains exactly a million bytes, closes it and then uses os.stat to verify that the file on disk is of the correct length (with os.stat, statinfo.st_size returns the size in bytes).

# Lesson4

Here are your instructions:

Make a FileHandling_Homework project and assign it to your Python2_Homework working set. In that project, write a module containing a function to examine the contents of the current working directory and print out a count of how many files have each extension (".txt", ".doc", etc.)

Write a separate module to verify by testing that the function gives correct results.

# Lesson5
Here are your instructions:


Write a function (not a class) that takes two arguments, a string player name and an integer score, and keeps a "high score" table in a Python shelve. If the integer argument is higher than the given player's current high score (or if the player has no recorded high score), log the value as this player's new high score. The function should return the player's current high score. Remember, a function is not the same thing as a class and it's a function that's needed.

Again, write a separate test module that verifies the operation of the function.



#Lesson 10
Here are your instructions:

Populate your database with "animal" and "food" tables using the tablepop and addfood programs that you wrote during the lesson (this step will not be necessary if you have not modified the tables since you created them in the lesson).

Write a program that verifies that every animal eats at least one food.

