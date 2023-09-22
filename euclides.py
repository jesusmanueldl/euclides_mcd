#MCD Auclides
def MCD_euclides(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


print(MCD_euclides(997,4))