# Computing the fine given the speed:
#   speed < 40 => no fine
#   speed 41 - 50 => $100
#   speed >50 => $200

def compute_fine(speed):
    if speed <= 40:
        fine = 0
    else:
        if speed <= 50:
            fine = 100
        else:
            fine = 200
    return fine

def compute_fine_2(speed):
    if speed <= 40:
        fine = 0
    elif speed <= 50:
        fine = 100
    elif speed <= 60:
        fine = 200
    else:
        fine = 300
    return fine
