def info():
    print("Hello user, what is your name, age and what is the current year? ")
    name = input("Enter your name: ")
    age = eval(input("Enter your age: "))
    year = eval(input("Enter the current year: "))
    year1 = year - age -1
    year2 = year - age 
    print("Dear " + str(name) + ", you were born either in " + str(year1) + " or " + str(year2))

info()
