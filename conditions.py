# Created by Vincent Tuberion
# conditions.py
# Date Created: 10/4/2021 11:48 EST
# Last Modified: 10/4/2021 12:03 EST
temp = 0
while temp != 999:
    temp = int(input("Please enter the current temperature or 999 to end:\n"))
    if temp == 999:
        print("Thank you for checking the temperature with us!")
    elif temp > 90 :  # temperature input is above 90 degrees
        print("Wear Shorts")
    elif 70 < temp <= 90:  # temperature input is above 70 degrees but only up to 90 degrees
        print("Short sleeves are fine")
    elif 50 < temp <= 70:  # temperature input is above 50 degrees but only up to 70 degrees
        print("Wear a jacket")
    elif 32 < temp <= 50:  # temperature input is above 32 degrees but only up to 50 degrees
        print("Wear a heavy coat")
    else:  # temperature input is not above 32 degrees
        print("Stay Inside")
