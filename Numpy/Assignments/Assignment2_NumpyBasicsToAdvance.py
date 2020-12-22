#Notes
#1) don't rename any function name
#2) don't rename any variable name
#3) don't remove any #comment 
#4) don't remove """ under triple quate values """
#5) you have to write code where you found "wrtie your code here"
#6) after download rename this file with this format "PIAICCompletRollNumber_AssignmentNo.py"
#   Example piaic17896_Assignment1.py
#7) After complete this assignment please push on your own github repository.
#8) you can submit this assignment through google form
#9) copy your this file absolute url then paste in google form
# Example above: https://github.com/EnggQasim/Batch04_to_35/blob/main/Sunday/1_30%20to%203_30/Assignments/assignment1.txt
# Because all assignment we will be cheked through software if you missed any above points
# then we can't assign your assignment numbers in our database.



import numpy as np

# Task no 1
def function1():
    # create 2d array from 1,12 range 
    # dimension should be 6row 2 columns  
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods  
    x =  np.arange(1,13).reshape((6,2)) 

    return x
    """
    expected output:
    [[ 1  2]
    [ 3  4]
    [ 5  6]
    [ 7  8]
    [ 9 10]
    [11 12]]
    """





