def is_palindrome(my_string):
    if len(my_string) <= 1:
        result = True
        return result
    if my_string[0] != my_string[-1]:
        return False

    return is_palindrome(my_string[1:-1])


print(is_palindrome("abba"))
print(is_palindrome("abcba"))
print(is_palindrome(""))
print(is_palindrome("abcd"))
