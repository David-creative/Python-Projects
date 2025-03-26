# Module 7 Project 7: Lottery Game

print("Welcome to the Ultimate Grand Lottery Game!")

# Ask the player for input for n possible numbers to guess from
n = int(input("Enter the total numbers of which k bets will be placed (n): "))

# Ask the player for input for guessing k nummbers
k= int(input("Enter number of bets that will be placed (k): "))

# Function to calculate factorial
def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Math to calculate n choose k
n_choose_k = fact(n)//(fact(n-k)*fact(k))

# Probability of winning big (hit all 5 drawn numbers)
print("Probability of winning big: ")
prob_big = 1 / (n_choose_k)
print(prob_big)

# Probability of winning little
print("Probability of winning little: (hitting k-1 drawn numbers): ")
prob_little = ((n-k)*(k)) / (n_choose_k)
print(prob_little)


#winning big math
#print(1 / (n_choose_k))

#winning little math
#print(((n-k)*(k)) / (n_choose_k))
