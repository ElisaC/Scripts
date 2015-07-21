import random

def generating_coordinates():
    lat = random.uniform(-90, 90)
    long = random.uniform (-180, 180)
    return lat , long

#print the result
print(generating_coordinates())
