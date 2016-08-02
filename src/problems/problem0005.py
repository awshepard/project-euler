# naive
def is_divisible_by_range(number, range_factor=20):
    for i in range(1,range_factor):
        if number % i != 0:
            return False
    return True

i = 20
while not is_divisible_by_range(i,20):
    i+=1

print i


# better:
# determine unique prime factors of all divisors, then multiply together
'''
1 *
2 
3 
2 2 
5 
2 3 
7 
2 2 2 
3 3 
2 5
11
2 2 3
13
2 7
3 5
2 2 2 2
17
2 3 3
19
2 2 5

2520 * 11 * 13 * 2 * 17 * 19 = 232792560 
'''
