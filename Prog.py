def Number1():
    return int(input("Enter your 1st number: "))

def Number2():
    return int(input("Enter your 2nd number: "))

def Number3():
    return int(input("Enter your 3rd number: "))

def Results(num1, num2, num3):
    result = num1 + num2 + num3
    print("The result is:", result)

n1 = Number1()
n2 = Number2()
n3 = Number3()
Results(n1, n2, n3)