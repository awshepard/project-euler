sum = 0
prev = 1
current = 2
while current < 4000000:
    if current%2 == 0:
        sum += current

    temp = current
    current += prev
    prev = temp

print sum
