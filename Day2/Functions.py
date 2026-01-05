# Day 02 - Functions
# Author: Rakshith

def add(a, b):
    """
    Adds two numbers.

    Parameters:
        a (int or float): first number
        b (int or float): second number

    Returns:
        int or float: sum of a and b
    """
    return a + b


def calculate_average(numbers):
    """
    Calculates average of a list of numbers.
    """
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


def normalize_scores(scores):
    """
    Normalize scores between 0 and 1.
    """
    min_score = min(scores)
    max_score = max(scores)

    normalized = []
    for s in scores:
        norm = (s - min_score) / (max_score - min_score)
        normalized.append(norm)

    return normalized
