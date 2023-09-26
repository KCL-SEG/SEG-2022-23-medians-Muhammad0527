"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import statistics


def median(list):
    list.sort()
    if len(list) % 2 == 1:
        return list[len(list) // 2]
    else:
        midValue = len(list) // 2
        num1 = list[midValue-1]
        num2 = list[midValue ]
        median = (num1 + num2) / 2
        return median

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        print(statistics.median(numbers))
        median = median(numbers)
        print(f'The median value is {median}')
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
#print(numbers)