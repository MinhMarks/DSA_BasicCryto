def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test the function
num1, num2 = map(int, input("Enter two numbers: ").split())
result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is", result)