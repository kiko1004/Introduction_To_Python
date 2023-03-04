1. Grade Calculator:
Write a program that takes a student's score out of 100 as input and prints out their corresponding letter grade (A, B, C, D, or F) based on the following grading scale:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60


<details>
<summary><b>Solution</b></summary>

```python
score = int(input("Enter student's score out of 100: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"The student's letter grade is {grade}")
```

</details>

<br>

2. Temperature Converter:
Write a program that takes a temperature input in Celsius and converts it to Fahrenheit or vice versa, based on the user's choice.

<details>
<summary><b>Solution</b></summary>

```python
temperature = float(input("Enter temperature: "))
unit = input("Enter temperature unit (C/F): ")

if unit == 'C':
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {fahrenheit}°F")
elif unit == 'F':
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {celsius}°C")
else:
    print("Invalid temperature unit. Please enter 'C' or 'F'.")
```

</details>
</br>

3. Positive or Negative:
Write a program that takes an integer as input and prints out whether it is positive, negative, or zero.

<details>
<summary><b>Solution</b></summary>

```python
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")
```

</details>
</br>


4. Leap Year:
Write a program that takes a year as input and prints out whether it is a leap year or not. A year is a leap year if it is divisible by 4, but not by 100, or if it is divisible by 400.

<details>
<summary><b>Solution</b></summary>

```python
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

```

</details>
</br>

5. Password Validator:
Write a program that takes a password as input and checks whether it meets the following requirements:

* At least 8 characters long
* Contains at least one uppercase letter
* Contains at least one lowercase letter
* Contains at least one number

<details>
<summary><b>Solution</b></summary>

```python
password = input("Enter a password: ")

# check if password is at least 8 characters long
if len(password) < 8:
    print("Password must be at least 8 characters long")
else:
    # check if password contains at least one uppercase letter
    has_uppercase = False
    for char in password:
        if char.isupper():
            has_uppercase = True
            break
    if not has_uppercase:
        print("Password must contain at least one uppercase letter")
    else:
        # check if password contains at least one lowercase letter
        has_lowercase = False
        for char in password:
            if char.islower():
                has_lowercase = True
                break
        if not has_lowercase:
            print("Password must contain at least one lowercase letter")
        else:
            # check if password contains at least one number
            has_number = False
            for char in password:
                if char.isnumeric():
                    has_number = True
                    break
            if not has_number:
                print("Password must contain at least one number")
            else:
                print("Password is valid")

```

</details>
</br>


