1. Write a program that takes an integer as input and prints out the sum of all numbers from 1 to that integer.

<details>
<summary><b>Solution</b></summary>

```python
num = int(input("Enter an integer: "))
sum = 0
for i in range(1, num + 1):
    sum += i
print("The sum of all numbers from 1 to", num, "is", sum)
```

</details>

<br>
2. Write a program that takes a string as input and prints out each character in the string on a separate line.

<details>
<summary><b>Solution</b></summary>

```python
string = input("Enter a string: ")
for char in string:
    print(char)
```

</details>

<br>

3. Write a program that takes a list of integers as input and prints out the average of those integers.

<details>
<summary><b>Solution</b></summary>

```python
num_list = [int(num) for num in input("Enter a list of integers, separated by spaces: ").split()]
sum = 0
for num in num_list:
    sum += num
average = sum / len(num_list)
print("The average of the numbers is", average)

```

</details>
<br>

4. Write a program that takes an integer as input and prints out all the factors of that integer.

<details>
<summary><b>Solution</b></summary>

```python
num = int(input("Enter an integer: "))
factors = []
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)
print("The factors of", num, "are", factors)


```

</details>

<br>

5. Write a program that takes two integers as input, and prints out all the prime numbers between those two integers.

<details>
<summary><b>Solution</b></summary>

```python
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
prime_numbers = []
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_numbers.append(num)
print("The prime numbers between", start, "and", end, "are", prime_numbers)
```

</details>

<br>