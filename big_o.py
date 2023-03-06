# O(1)
"""For finding the pe of the first stock in your list"""
def find_first_pe(prices, eps, index):
    pe = prices[index] / eps[index]
    return pe

# O(n)
"""The time it takes to run this function is directly proportional to the size of the input."""
def get_squared_numbers(numbers):
    squared_numbers = []
    for number in numbers:
        squared_numbers.append(number * number)
    return squared_numbers
numbers = [1, 2, 3, 4, 5]
# print(get_squared_numbers(numbers))

# O(n^2)
"""The time it takes to run this function is proportional to the square of the size of the input."""
# Finding the duplicate from a list of numbers
numbers = [3, 4, 6, 7, 3, 2, 6, 1, 3]
duplicate = None
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate = numbers[i]
            break
for i in range(len(numbers)):
    if numbers[i] == duplicate:
        print(i)
"""
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print("Duplicate found: {}".format(numbers[i]))
            break
"""
# Keep fastest growing term
# Drop constants
# iterations k = n/2^K
"""
1 = n/2^K
n = 2^K
log2(n) = log2(2^K)
log2(n) = Klog2(2)
K = log(n)
"""