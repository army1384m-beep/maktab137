# قسمت اول
" Positional-Only (/) فقط با جایگاه میشناسه نه با اسم "
def add_numbers(num1, num2, /):
    return num1 + num2

print(add_numbers(5, 3))        
print(add_numbers(10, 20))      
print(add_numbers(-2, 7))       


# قسمت دوم
"Keyword-Only (*)فقط با اسم میشناسه، نه با جایگاه"
def print_info(*, name, age):
    print(f"Name: {name}, Age: {age}")

print_info(name="Ali", age=25)
print_info(age=30, name="Maryam")
print_info(name="Reza", age=18)


# قسمت سوم
def calculator(num1, num2, /, *, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Invalid operator"

print(calculator(10, 5, operation="+"))    
print(calculator(10, 5, operation="-"))    
print(calculator(10, 5, operation="*"))    
print(calculator(10, 5, operation="/"))    

