#David Ayriyan
#Module 3 Project 3: GP's

def n_th(a, r, n):
    return a * r ** (n-1)


def sum(a, r, n):
    # acc = 0
    # for i in range(n):
    #     acc += GP(a, r, i+1)
    # print("The sum is:", acc)
    if (r == 1):
        print("This GP converges with infinite elements to", a * n)
    elif (r == -1) and (n % 2 == 1):
        print("The sum is:", a)
    elif (r == -1) and (n % 2 == 0):
        print("The sum is:", 0)
    else:
        print("Use another formula")


# first element
a = float(input("Enter scale factor a:"))

# number to multiply each element by
r = float(input("Enter common ratio r:"))

