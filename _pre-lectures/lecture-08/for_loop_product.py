primes = [2, 3, 5, 7]
prod = 1
for n in primes:
    print('start: n = ' + str(n) + '; prod = ' + str(prod))
    prod *= n
    print('end:   n = ' + str(n) + '; prod = ' + str(prod))

print(prod)
