# CSC 6023: Advanced Algorithms
# David Ayriyan
# Module 03: Project 03

# Tribonacci Function
def tribo(n):
    a, b, c = 1, 1, 1
    # n < 4 since a,b,c are for first three numbers
    if (n < 4):
        return 1
    for _ in range(3, n):
        # add c variable
        a, b, c = b, c, a + b + c
    return c

def main():
    
    while True:
        # try-except block to take into acount non-number input
        try:    
            n = int(eval(input("Choose an Integer. An integer less than 1 ends the program: ")))
        except NameError:
            print("Please enter a valid integer number to insert into the tree.")
            continue
        
        # ends program if user input n < 1
        if n < 1:
            print("You ended the program. Good-bye.")
            break
        else:
            print("The {}-th element of Tribonacci is {}".format(n,tribo(n)))
            continue
    
# calling main block
if  __name__ == "__main__":
    main()
