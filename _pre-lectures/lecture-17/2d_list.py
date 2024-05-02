cities = ["San Diego", "Anaheim", "Las Vegas"]
wdata = [[77, 77, 76, 74, 73], 
         [85, 85, 78, 81, 81],
         [104, 106, 101, 97, 97]]

print(wdata)
print()
print()

'''
for r in range(len(wdata)):
    #print(wdata[r])
    for c in range(len(wdata[r])):
        #print(wdata[r][c])
        print("r = " + str(r) + " | c = " + str(c) + " | value = " + str(wdata[r][c]))
    print("--------------------------------")
'''

for r in range(len(wdata)):
    total = 0
    for c in range(len(wdata[r])):
        total += wdata[r][c]
    avg = total / len(wdata[r])
    print(cities[r] + ": avg temp = " + str(avg))
    print("--------------------------------")


print("Program is over.")
