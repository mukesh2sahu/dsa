def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    return original == reverse

# Example
print(is_palindrome(121))  # True
print(is_palindrome(123))  # False
