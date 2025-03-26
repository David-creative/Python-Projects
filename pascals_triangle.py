# Module 5 Project 5: Pascal's Triangle

# Ask the user the number of lines in triangle (range: 4-8)
print("Pascal Triangle Maker.")
num_lines = int(input("Enter the number of lines (4 to 8): "))

#Function to calculate the binomial coefficient
def comb(n, k):
    if k == 0 or k == n:
        return 1
    return comb(n - 1, k - 1) + comb(n - 1, k)

print(comb(5,3))



# def comb(k,n):
#    ans = 1
#    if (k > n//2):
#        k = n-k
#    for i in range(k):
#        ans *= (n-i) / (i+1)
#    return ans

# Function to print Pascal's Triangle
def pascals_triangle(num_lines):
    for line in range(num_lines):
        for i in range(num_lines - line):
            print(" ", end=" ")
        for i in range(line + 1):
            coefficient = comb(line, i)
            print(f"{coefficient:^4}", end=" ")
        print() 

# Code to take into account input thats not between 4 and 8
if num_lines > 3 and num_lines < 9:
    pascals_triangle(num_lines)
else:
    print("PLease enter a number between 4 and 8.")


