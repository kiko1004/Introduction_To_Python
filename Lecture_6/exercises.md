1. Create a class called Rectangle with attributes width and height. Add a method called area that calculates and returns the area of the rectangle.

<details>
<summary><b>Solution</b></summary>

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

```

</details>

<br>
2. Create a class called Person with attributes name, age, and gender. Add a method called get_older that increases the person's age by 1.

<details>
<summary><b>Solution</b></summary>

```python
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_older(self):
        self.age += 1


```

</details>

<br>


3. Create a class called BankAccount with attributes balance and interest_rate. Add methods called deposit and withdraw that modify the account balance accordingly.

<details>
<summary><b>Solution</b></summary>

```python
class BankAccount:
    def __init__(self, balance=0, interest_rate=0.05):
        self.balance = balance
        self.interest_rate = interest_rate
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

```

</details>

<br>

4. Create a class called Dog with attributes name and breed. Add a method called bark that prints "Woof!".

<details>
<summary><b>Solution</b></summary>

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print("Woof!")


```

</details>

<br>

5. Create a class called Car with attributes make, model, and year. Add a method called start_engine that prints "Vroom!"

<details>
<summary><b>Solution</b></summary>

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print("Vroom!")


```

</details>

<br>

6. Create a class called Student with attributes name, major, and gpa. Add a method called graduate that returns True if the student's GPA is greater than or equal to 3.0, and False otherwise.

<details>
<summary><b>Solution</b></summary>

```python
class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    
    def graduate(self):
        return self.gpa >= 3.0


```

</details>

<br>

7. Create a class called Shape with a method called draw that prints "Drawing a shape". Create subclasses Circle, Square, and Triangle that override the draw method to print "Drawing a circle", "Drawing a square", and "Drawing a triangle", respectively.

<details>
<summary><b>Solution</b></summary>

```python
class Shape:
    def draw(self):
        print("Drawing a shape")
    
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle")



```

</details>

<br>

8. Create a class called Bank with a dictionary attribute accounts that maps account names to BankAccount objects. Add methods called create_account, get_account_balance, and set_account_balance that allow the user to create new accounts, check the balance of an account, and set the balance of an account, respectively.

<details>
<summary><b>Solution</b></summary>

```python
class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, name, balance=0):
        if name in self.accounts:
            raise ValueError("Account already exists")
        self.accounts[name] = BankAccount(balance)
    
    def get_account_balance(self, name):
        if name not in self.accounts:
            raise ValueError("Account does not exist")
        return self.accounts[name].balance
    
    def set_account_balance(self, name, balance):
        if name not in self.accounts:
            raise ValueError("Account does not exist")
        self.accounts[name].balance = balance




```

</details>

<br>


9. Create a class called Deck with a list attribute cards that represents a deck of cards. Add methods called shuffle and deal that shuffle the deck and deal a card from the top of the deck, respectively.

<details>
<summary><b>Solution</b></summary>

```python
import random

class Deck:
    def __init__(self):
        self.cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop(0)

```

</details>

<br>
