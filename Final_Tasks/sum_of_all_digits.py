# Write a program that calculates the sum of the digits of a given number.
def digit_sum(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total
