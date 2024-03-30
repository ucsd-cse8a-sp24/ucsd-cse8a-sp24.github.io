def km_to_miles(dist_km):
    dist_miles = dist_km / 1.609
    return dist_miles

d_km = float(input('Enter distance in km: '))
d_mi = km_to_miles(d_km)
print("distance in miles = " + str(d_mi))

