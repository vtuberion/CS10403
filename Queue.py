# Created by Vincent Tuberion
# Queue.py
# Date Created: 11/28/2021 17:44 EST
# Last Modified: 11/28/2021 : EST

names = []

while len(names) < 10:
    acceptedName = input("Please insert a name (" + str(len(names) + 1) + " / 10):\n")
    names.append(acceptedName)

i = 0
while i < len(names):
    print(names.pop(i))
