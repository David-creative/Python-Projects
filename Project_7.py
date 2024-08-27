# CSC 6013
# David Ayriyan
# Project 7: Develop program to perform Quick Select algorithm 

from random import randint

# Quick select algorithm
def QuickSelect(A, k):
    # adjusts value of k because list indices are 0 based
    k = k- 1

    def lomuto(left,right):
        # chooses last element in array as pivot
        p = A[right]
        # initializes index of smaller element
        i = left
        # iterates through array from left to right-1
        for j in range(left, right):
            if A[j] < p:
                # swaps elements at these indices
                A[i], A[j] = A[j], A[i]
                i += 1
        # swap pivot element with element at index 'i'
        A[i], A[right] = A[right], A[i]

        # if pivot's index 'i' is greater than 'k', apply lomuto function again to
        # left subarray 
        if i > k:
            return lomuto(left, i-1)
        # if pivot's index 'i' is less than 'k', apply lomuto function again to
        # right subarray 
        elif i < k:
            return lomuto(i+1, right)
        # when i=k, have found k-th smallest element
        else:
            return A[i]
    # calls lomuto function with defined arguments
    return lomuto(0, len(A)-1)

def main():
    # initialize array 'A'
    A = []
    # sets n to '1000'
    n = 1000

    # ensures each number is unique; adds to array if it is
    # will generate 1000 unique random numbers within the array 'A'
    for _ in range(n):
        r = randint(1,100000)
        while r in A:
            r = randint(1, 100000)
        
        A.append(r)

    # Prompts user for input of 'k'
    k = int(input("Enter the value of kth smallest element that you want to find: "))
    print("This is the",k,"th smallest element in the array 'A':",QuickSelect(A, k))


# calling main block
if  __name__ == "__main__":
    main()