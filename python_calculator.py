# Display calculator heading
print("----- Calculator -----")

# Take first number input from user
number1 = int(input("Enter the first number : "))

# Take second number input from user
number2 = int(input("Enter the second number : "))

# Take operator input from user
operator = input('Enter the operator : ')

# Check if operator is addition
if operator == "+":
    print("The sum of number is :",number1, '+' ,number2, "="  ,number1 + number2)

# Check if operator is subtraction
elif operator == "-":
    print("The subtraction of number is :",number1, '-' ,number2, "="  , number1 - number2)

# Check if operator is multiplication
elif operator == "*":
    print("The multiplication of number is :",number1, '*' ,number2, "="  , number1 * number2)

# Check if operator is division
elif operator == "/":
    print("The division of number is :",number1, '/' ,number2, "="  , number1 / number2)

# Check if operator is modulo
elif operator == "%":
    print("The modulo of number is :",number1, '%' ,number2, "="  , number1 % number2)

# Check if operator is power
elif operator == "**":
    print("The power of number is :",number1, '^' ,number2, "="  , number1 ** number2)

# If operator is invalid
else:
    print("Invalid operator\n","Try use another opeartor - [ '+','-','*','/','%','**' ]")
        
# Display calculation completed message
print("Calculation Done")