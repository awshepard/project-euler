import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

largest = 1
for i in range(1,int(math.sqrt(600851475143))+1):
    if 600851475143%i == 0 and is_prime(i):
        largest = i

print largest
