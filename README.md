# Python2_oreillyschool.com
# Python2 
# http://courses.oreillyschool.com/Python2/index.html
# Lesson 2 Unit Testing 

Here are your instructions:


Make a UnitTesting_Homework project and assign it to the Python2_Homework working set. In this project, write a unittest test program for the following function. (The test program makes unittest.TestCase assertions about the results of calling the function with known arguments.)
def title(s):
    "How close is this function to str.title()?"
    return s[0].upper()+s[1:]
Test your results for a given string s by comparing them with s.title(). Because this is purely an exercise, it's OK to put your test code in the same file as the function and just hand in a single file. Your file should be an importable module. You should be able to find an example that shows title(s) and s.title() diverge (have different output). Bonus marks for fixing the error in the function above (making it behave more like the native method).


# Lesson 3 Test-Driven Development 

Here are your instructions:


Make a TestDrivenDevelopment_Homework project and assign it to the Python2_Homework working set.

Copy the setupDemo.py file from the TestDrivenDevelopment/src folder to the TestDrivenDevelopment_Homework/src folder.

Modify it so that:
•The test_1() method includes code to verify that the test directory contains only the files created by the for loop. Hint: You might create a set containing the list of three filenames, and then create a set from the os.listdir() method.
•A test_3() method creates a binary file that contains exactly a million bytes, closes it and then uses os.stat to verify that the file on disk is of the correct length (with os.stat, statinfo.st_size returns the size in bytes).

# Lesson 4 File Handling 

Here are your instructions:

Make a FileHandling_Homework project and assign it to your Python2_Homework working set. In that project, write a module containing a function to examine the contents of the current working directory and print out a count of how many files have each extension (".txt", ".doc", etc.)

Write a separate module to verify by testing that the function gives correct results.

# Lesson 5 Persistent Storage 
Here are your instructions:


Write a function (not a class) that takes two arguments, a string player name and an integer score, and keeps a "high score" table in a Python shelve. If the integer argument is higher than the given player's current high score (or if the player has no recorded high score), log the value as this player's new high score. The function should return the player's current high score. Remember, a function is not the same thing as a class and it's a function that's needed.

Again, write a separate test module that verifies the operation of the function.

# Lesson 6 Archives

Here are your instructions:

The zipfile example in the lesson text stores the full path of the files that it saves to the zipfile. Normally, however, zipfiles contain only a relative pathname (you will see that when the names are listed after the zipfile is created, the "v:\\" has been removed).

Create a project named Archives_Homework and add it to the Python2_Homework working set. In this project, write a function that takes a directory path and creates an archive of the directory only. For example, if the same path were used as in the example ("v:\\workspace\\Archives\\src\\archive_me"), the zipfile would contain "archive_me\\groucho" "archive_me\\harpo" and "archive_me\\chico."

Note that zipfile.namelist() always uses forward slashes in what it returns, a fact you will need to accommodate when comparing observed and expected.

The base directory ("archive_me" in the example above) is the final element of the input, and all paths recorded in the zipfile should start with the base directory.

If the directory contains subdirectories, the subdirectory names and any files in the subdirectories should not be included. (Hint: You can use isfile() to determine if a filename represents a regular file and not a directory.)

# Lesson 7 Introduction to Graphical User Interfaces 

Write a GUI-based program that provides two Entry fields, a button and a label. When the button is clicked, the value of each Entry should (if possible) be converted into a float. If both conversions succeed, the label should change to the sum of the two numbers. Otherwise it should read "***ERROR***."


# Lesson 8 Graphical User Interface Layout 

Here are your instructions:

Write a GUI-based program to build a window layout as shown below. When the frame is resized, the buttons should stay the same height and expand sideways. Frame 1 and Frame 2 should always be the same height and width as each other, and Frame 3 should be half as wide again as they are (i.e. 150% wider, as shown below).  Labeling each Frame is optional / good exercise.
+---------------------+--------------------------------+
|                     |                                |
|                     |                                |
|                     |                                |
|      Frame 1        |                                |
|                     |                                |
|                     |                                |
|                     |                                |
+---------------------+               Frame 3          |
|                     |                                |
|                     |                                |
|                     |                                |
|     Frame 2         |                                |
|                     |                                |
|                     |                                |
+----------+----------+----------+----------+----------+
| Button 1 | Button 2 | Button 3 | Button 4 | Button 5 |
+----------+----------+----------+----------+----------+



# Lesson 9 More About Graphical User Interfaces 


Starting with the project you created at the end of the last lesson, add components to the existing framework so that:
•When an area occupied by Frame 1 or Frame 2 is clicked with mouse button 1, the program should print which frame was clicked and the X and Y coordinates (relative to the Frame).
•Frame 3 should contain an Entry and a Text widget. When the button now labeled "Open" is clicked, the content of the Entry should be used as a file name, and the content of the file (if any) displayed in the Text widget.
•The Entry and Text widgets should completely fill Frame 3 and continue to do so even as the application window is resized.
•The color of the text displayed in Frame 3's Text widget should change appropriately when the "Red," "Blue," "Green," or "Black" buttons are clicked.
+---------------------+--------------------------------+
|                     |                                |
|                     |                                |
|                     |                                |
|      Frame 1        |                                |
|                     |                                |
|                     |                                |
|                     |                                |
+---------------------+               Frame 3          |
|                     |                                |
|                     |                                |
|                     |                                |
|     Frame 2         |                                |
|                     |                                |
|                     |                                |
+----------+----------+----------+----------+----------+
|    Red   |   Blue   |  Green   |  Black   |   Open   |
+----------+----------+----------+----------+----------+

# Lesson 10 Handling Databases 
Here are your instructions:

Populate your database with "animal" and "food" tables using the tablepop and addfood programs that you wrote during the lesson (this step will not be necessary if you have not modified the tables since you created them in the lesson).

Write a program that verifies that every animal eats at least one food.

# Lesson 11 Database Hints and Tricks 

Here are your instructions:


Modify the classFactory.py source code so that the DataRow class returned by the build_row function has another method:

retrieve(self, curs, condition=None)

self is (as usual) the instance whose method is being called, curs is a database cursor on an existing database connection, and condition (if present) is a string of condition(s) which must be true of all received rows.

The retrieve method should be a generator, yielding successive rows of the result set until it is completely exhausted. Each row should be a next object of type DataRow.


# Lesson 12 Handling Electronic Mail Messages 

Here are your instructions:


Write a function that takes an email address, a string, and a list argument. It should return an email message addressed to the email address passed as the first argument, with the second argument as the message body. If the list is non-empty, then each list item should be treated as the name of a file and the corresponding file should be attached (with an appropriate MIME type) to the message.

Please include any files to attach in the same folder as your program. There is no need to send it as an email with smtp, though you may wish to print it as a string as a part of testing.

# Lesson 13 Email Search and Display 

Here are your instructions:


Write a program that imports the following names from a "settings" module:
RECIPIENTS   a list of (name, email-address) tuples
STARTTIME    datetime.datetime object for first message
DAYCOUNT    number of daily message generations

The program should produce a message of the format:
Date: {{date}}
From: <a href="mailto:website@example.com">website@example.com</a>
To: {{recipient}}
Message-Id: <NNNNNN>

This is a test message.

Your program should save these messages in the messages table.

Use test-driven development, and state the purpose of each test in the suite in docstrings that will eventually document your program.

Time your program for DAYCOUNTS of 1, 10, 50, 100, and 500 and plot the results (on a sheet of paper). How reliable are the timings?

Think of it like this: You are soon to go on vacation, at STARTTIME, for DAYCOUNT days, and you want your co-workers (RECIPIENTS) to continue getting your famous Joke of the Day (JOTD).

Your strategy is to store up the emails ahead of time, predated with the date they're to be sent. So if you leave on vacation on Jan 3, 2013, the first set of emails might be dated Jan 4 (each recipient gets one), then Jan 5 and so on, for DAYCOUNT days.

A good test that you have the right number is DAYCOUNT * len(RECIPIENTS) should equal SELECT COUNT(*) FROM jotd_emails; that is, the total number of days you're on vacation times the number of receivers, should equal the total number of records in the table generated. Of course, this will only be true if your To: line is only to a single recipient, and not all of them separated by commas.

Storing the right date for each email will likely involve using a timedelta to increment a datetime by one day at a time for DAYCOUNT days.

Regarding timing, it's enough to count under your breath and give a sense in your remarks about how you think time might be a function of DAYCOUNT. If you have your email generating and storing function where you might conveniently go:
    start = time.time()
    call_function(args)
    end = time.time()
    interval = end - start
    print("Time to complete: ", end)

Then you could also give some hard numbers as to the relative times the program took as a function of changing DAYCOUNT. The purpose of this requirement is to look ahead to future projects where timing / profiling is a core focus.
