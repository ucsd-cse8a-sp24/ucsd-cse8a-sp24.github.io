G = 1

def incr(P):
    A = P + G
    return A

def incr2(P):
    A = P + G
    B = incr(A)
    return B

z = incr2(3)
