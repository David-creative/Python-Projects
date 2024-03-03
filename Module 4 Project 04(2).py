# Module 4 Project 4: Computing Arrangements of Multisets

# Ask the user the number of subsets (no smaller than 3, no greater than 8)
j = int(input("Enter the number of subsets (between 3 and 8): "))

# Ask the user the size of each subset (from 1 to 5)

#initializing dictionary to add values to it
#has to be outside the loop because you would reset and lose data in the for loop 
data_dict = {}

#for loop to ask question the correct number of times
for m in range(1, j+1):
    # creates a key/value pair for each number between 1 and j
    # the key will be the variable number from the loop and the value will be th user inputed value
    # f'string' means format the string. It will replace {m} with the actual number from the range
    data_dict[m] = int(input(f"Enter the size of the subset {m} (between 1 and 5): "))

# n is the P(sum) of the sizes of each subset
# total number of arrangements (smaller than sum of sizes of subsets)
k = int(input("Enter the total number of arrangements (smaller than the sum of subset sizes): "))

# Program to find sum of all items in a Dictionary
# Function to print sum
def returnSum(data_dict):
 
    sum = 0
    for i in data_dict:
        sum = sum + data_dict[i]
    
    return sum

print("Sum of everything in dictionary: ", returnSum(data_dict))

#makes n equal the sum of all values in the dictionary
n = returnSum(data_dict)

# Getting all the values of a dictionary as a list
list_of_the_values = list(data_dict.values())

# Printing the list which contains all the values of the dictionary
#print(list_of_the_values)
    
# pair of functions used to calculate the number of arragements
def fact(n):
    acc = 1
    for i in range(2, n+1):
        acc *= i
    return acc

def arrangement(k, n):
    return fact(n) // fact(n-k)

# function used to caluclate factorial of subsets sizes then multiplying them
def fact_sizes():
    acc = 1
    for i in data_dict.values():
        acc *= fact(i)
    return acc

# total number of arrangements considering the subsets sizes
total = fact(n) // (fact(n-k) * fact_sizes())

print(f"The number of arrangements of {k} elements out of {n} considering the subsets sizes {list_of_the_values} is: {total}")
