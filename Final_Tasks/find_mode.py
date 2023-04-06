from collections import Counter

def calculate_mode(numbers):
    frequency = Counter(numbers)
    max_count = max(frequency.values())
    return [number for number, count in frequency.items() if count == max_count]
