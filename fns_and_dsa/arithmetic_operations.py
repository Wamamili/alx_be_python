def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations on two numbers.

    Parameters: num1 , num2
    - operation (str): The operation to perform - 'add', 'subtract', 'multiply', or 'divide'

    Returns:
    - float or str: result of arithmetic operation or error message if operation is invalid
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
