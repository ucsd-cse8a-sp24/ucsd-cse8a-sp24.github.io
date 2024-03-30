hours = float(input('enter hours: '))

while hours < 0 or hours > 168:
    print('Invalid number of hours. Please try again...')
    hours = float(input('enter hours: '))

print("Valid number of hours. Accepted!")

