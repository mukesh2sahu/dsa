def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]

# Example
print(is_palindrome(121))  # True
print(is_palindrome(123))  # False
