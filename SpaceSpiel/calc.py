PI = 3.14

def addition(a,b):
    return a+b
def faculty(num):
    if num < 0 :
        return 0
    if num == 0 :
        return 1
    facultät = 1
    for i in range(1,num+1):
        facultät = facultät * i
    return facultät
