# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

# Variables to represent the grade thresholds
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Get a test score from the user.
test1 = float(input('Enter the score for Component 1: '))
test2 = float(input('Enter the score for Component 2: '))
test3 = float(input('Enter the score for Component 3: '))

# Calculate the average test score.
score = (test1 + test2 + test3) / 3
print('The average score is', format(score,'.2f'))
#score = int(input('Enter your test score: '))
 
# Determine the grade.
if score >= A_score:
    print('Your grade is A.')
elif score >= B_score:
    print('Your grade is B.')
elif score >= C_score:
    print('Your grade is C.')
elif score >= D_score:
    print('Your grade is D.')
else:
    print('Your grade is F.')
# End of if-elif structure



    

