# Created by Vincent Tuberion
# Average.py
# Date Created: 9/29/2021 16:10 EST
# Last Modified: 9/29/2021 16:20 EST

average = 0
total = 0
howManyEntered = 0
howMany = int(input('How many test scores would you like to average?\n'))
while howManyEntered < howMany:
    testScore = int(input('Enter test score:\n'))
    total = total + testScore
    howManyEntered += 1
average = total / howMany
print('The average for the test scores you entered is: ' + str(round(average, 2)))
