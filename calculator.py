import math

op = input("Enter the operator:")
if op == 'sqr' or op == '%' or op == 'sin' or op == 'cot' or op == 'tan' or op == 'fac':
    a = float(input("Enter the number:"))
else:
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))

# sum
if op == '+':
    result = a + b
# subtraction
elif op == '-':
    result = a - b
# division
elif op == '/':
    if b == 0:
        result = "Cannot divide by zero"
    else:
        result = a / b
# multiplication
elif op == '*':
    result = a * b
# cent
elif op == '%':
    result = a / 100
# power
elif op == '^':
    result = a ** b
# logarithm
elif op == 'log':
    result = math.log(a, b)
# square
elif op == 'sqr':
    result = math.sqrt(a)
# sinus
elif op == 'sin':
    c = (a / 180) * math.pi
    result = math.sin(c)
# cotangent
elif op == 'cot':
    c = (a / 180) * math.pi
    result = 1 / math.tan(c)
# tangent
elif op == 'tan':
    c = (a / 180) * math.pi
    result = math.tan(c)
#factorial
elif op == 'fac':
    result = math.factorial(a)

else:
    result = 'error!'
print("Answer:"+ "  "+ str(result))
