total = 0
count = 0

while True:
    rainfall = int(input('rainfall: '))
    if rainfall == 99999:
        break
    if rainfall >= 0:
        total += rainfall
        count += 1

if count > 0:
    print('number of valid days = ' + str(count))
    avg = total / count
    print('average rainfall = ' + str(avg))
elif count == 0:
    print('no rainfall')

