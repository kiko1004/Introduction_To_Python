1. Create a tuple of your favorite fruits and print it to the console.

<details>
<summary><b>Solution</b></summary>

```python
fruits = ('apple', 'banana', 'orange', 'mango', 'kiwi')
print(fruits)

```

</details>

<br>

2. Create a new tuple by concatenating two tuples together.

<details>
<summary><b>Solution</b></summary>

```python
tuple2 = (1, 2, 3)
tuple3 = (4, 5, 6)
tuple4 = tuple2 + tuple3
print(tuple4)


```

</details>

<br>

3. Create a new tuple with a single element.

<details>
<summary><b>Solution</b></summary>

```python
tuple6 = ('hello',)
print(tuple6)
```

</details>

<br>

<br>

4. Write a program that takes a tuple of numbers and returns the sum of all the even numbers in the tuple.

<details>
<summary><b>Solution</b></summary>

```python
def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(sum_even_numbers(my_tuple))

```
</details>
<br>

5. Create a new set that contains only the common elements of the following two sets.

<details>
<summary><b>Solution</b></summary>

```python
set2 = {1, 2, 3, 4}
set3 = {3, 4, 5, 6}
common_set = set2.intersection(set3)
print(common_set)
```
</details>
<br>

6. Write a program that takes two tuples and returns a tuple of all the elements that are common to both tuples.

<details>
<summary><b>Solution</b></summary>

```python
def common_elements(tuple1, tuple2):
    set1 = set(tuple1)
    set2 = set(tuple2)
    common = set1.intersection(set2)
    return tuple(common)

t1 = (1, 2, 3, 4, 5)
t2 = (3, 4, 5, 6, 7)
print(common_elements(t1, t2))
```
</details>
<br>

7. Suppose you are organizing a party and want to keep track of the guests, their preferred drinks, and their dietary restrictions. Write a program that does the following:

Define a set drinks that contains the types of drinks that will be available at the party: "water", "juice", "soda", and "beer".
Define a tuple guest_list that contains the names of all the guests who will be attending the party.
Define a dictionary preferences that maps each guest's name to a tuple of their preferred drink and their dietary restrictions. For example, preferences["Alice"] = ("juice", "vegetarian") means that Alice prefers juice and is a vegetarian.
Print out the name of each guest and their preferred drink, one line at a time.

<details>
<summary><b>Solution</b></summary>

```python
# Define the set of drinks
drinks = {"water", "juice", "soda", "beer"}

# Define the tuple of guests
guest_list = ("Alice", "Bob", "Charlie", "Dave", "Eve")

# Define the dictionary of preferences
preferences = {
    "Alice": ("juice", "vegetarian"),
    "Bob": ("beer", "omnivore"),
    "Charlie": ("soda", "vegan"),
    "Dave": ("water", "pescatarian"),
    "Eve": ("juice", "gluten-free")
}

# Print out each guest's name and preferred drink
for guest in guest_list:
    drink, restriction = preferences[guest]
    print(guest + " prefers " + drink)
```
</details>
<br>



