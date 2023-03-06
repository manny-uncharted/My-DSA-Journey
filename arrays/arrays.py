import numpy as np

my_array = np.array([1,2,3,4,5,6,7,8,9,10])

# use floating point numbers
float_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10], dtype=np.float64)

# indexing arrays
print(my_array[0])

# modify array
my_array[0] = 100

# addition of arrays
array1 = np.array([1,2,3,4,5])
array2 = np.array([6,7,8,9,10])

result = array1 + array2
print(result)

# multiplication of arrays
result_mult = array1 * array2
print(result_mult)


# Mimimum and maximum values
min_val = np.min(array1)
max_val = np.max(array1)
print(f"The minimum value is {min_val} and the maximum value is {max_val}.")

# Sort the elements of an array
array3 = np.array([4,7,9,1,5,8,3,2])
sorted_array = np.sort(array3)
print(sorted_array)

# reverse array: Arranges the sorted array in descending order
reversed_array = np.flip(sorted_array)
print("The reversed array is {}".format(reversed_array))

# calculate the mean of an array
mean = np.mean(array3)
print("The mean of the array is {}".format(mean))

# calculate the median of an array
median = np.median(array3)
print("The median of the array is {}".format(median))

# calculate the standard deviation of an array
std = np.std(array3)
print("The standard deviation of the array is {}".format(std))

# Matrices
matrix1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix2 = np.array([[10,11,12],[13,14,15],[16,17,18]])

# multiply matrices
result_matrix = np.dot(matrix1, matrix2)
print("The result of the matrix multiplication is {}".format(result_matrix))

# transpose a matrix
transposed_matrix = np.transpose(matrix1)
print("The transposed matrix is {}".format(transposed_matrix))

