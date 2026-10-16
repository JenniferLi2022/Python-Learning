print("=== Example 1: Basic Function ===")
def greet(name):
    message = "Hello, " + name
    return message

result = greet("Alice")
print(result)

print("")

print("=== Example 2: Mltiple Parameters ===")
def add(a,b):
    return a + b

sum_result = add(5,3)
print("5 + 3 = " + str(sum_result))

print("")

print("=== Example 3: Default Parameter ===")
def greet_formal(name,greeting="Hello"):
    return greeting + ", " + name

print(greet_formal("Alice"))
print(greet_formal("Bob","Hi"))

print("")

print("=== Example 4: Calculate ===")
def calculate(a,b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    return addition,subtraction,multiplication,division

add_result,sub_result,mul_result,div_result = calculate(10,2)
print("Addition: " + str(add_result))
print("Subtraction: " + str(sub_result))
print("Multiplication: " + str(mul_result))
print("Division: " + str(div_result))

print("")

print("=== Example 5: Function With List ===")
def sum_list(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

numbers = [1,2,3,4,5]
result = sum_list(numbers)
print("Sum of " + str(numbers) + " is " + str(result))

print("=== Example 6: Funtion with Dictionary ===")
def get_student_info(student):
    name = student["name"]
    age = student["age"]
    score = student["score"]
    return name + " is " + str(age) + " years old with score " + str(score)

student_info = {"name": "Alice", "age": 20, "score": 95}
print(get_student_info(student_info))

print("")

print("=== Example 7: Multiple Functions ===")
def get_square(x):
    return x * x

def get_sum_of_squares(a,b):
    return get_square(a) + get_square(b)

result = get_sum_of_squares(3,4)
print("3^2 + 4^2 = " + str(result))
