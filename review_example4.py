def calculate(a,b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    return addition, subtraction, multiplication, division

add_result, sub_result, mul_result, div_result = calculate(10,2)
print("Addition: " + str(add_result))
print("Subtraction: " + str(sub_result))
print("Multiplication: " + str(mul_result))
print("Division: " + str(div_result))

