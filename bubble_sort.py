"""_summary_
    Bubble Sort Demonstration
"""

numbers = [8, 6, 7, 5, 3, 0, 9]
print(f"numbers = {numbers}")

# numbers.sort()
# new_order = sorted(numbers)
# print(f"new_order = {new_order}")
# print(f"numbers = {numbers}")

swapped = True  # flag set to boolean value of True

while swapped:  # while swapped = True
    swapped = False
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            swapped = "True"
print(f"numbers = {numbers}")
