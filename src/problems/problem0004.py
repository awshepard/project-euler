
def is_palindrome(n):
    if not isinstance(n,basestring):
        n = str(n)
    length = len(n)
    for i in range(0,length/2):
        if n[i] != n[length-1-i]:
            return False
    return True

largest = -1
for i in range(100,1000):
    for j in range(100,1000):
        product = i * j
        if is_palindrome(product) and product > largest:
            largest = product


print largest

