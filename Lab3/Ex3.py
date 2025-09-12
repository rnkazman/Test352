def squareroot(x, precision=2):
    """Compute the square root of x."""
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    return round(x ** 0.5, precision)

value_from_user = float(input("Enter a number to find its square root: "))
result = squareroot(value_from_user)
print(f"The square root of {value_from_user} is {result}")
