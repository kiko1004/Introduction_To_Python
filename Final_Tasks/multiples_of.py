# calculates the sum of all the multiples of 3 or 5 below a specified number
def multiples_sum(n):
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])
