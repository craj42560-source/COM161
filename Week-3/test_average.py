# This program gets three test scores and displays
# their average.  It congratulates the user if the
# average is a high score.

# The high score variable holds the value that is
# considered a high score.
high_score = 70
low_score=50
 
# Get the three test scores.
test1 = float(input('Enter the score for test 1: '))
test2 = float(input('Enter the score for test 2: '))
test3 = float(input('Enter the score for test 3: '))
test4 = float(input('Enter the score for test 4: '))

# Calculate the average test score.
average = (test1 + test2 + test3 +test4) / 4

# Print the average.
print('The average score is', format(average,'.2f'))

# If the average is a high score,
# congratulate the user.
if average >= high_score:
    print('Congratulations!')
    print('That is a great average!')
if average < low_score:
    print('You need to work hard in the future :!')

