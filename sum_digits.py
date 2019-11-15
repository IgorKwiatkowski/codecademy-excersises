# def sum_digits(n, result=0):
#
#     if n <= 9:
#         result += n
#         return result
#     else:
#         result += int(str(n)[0])
#         print(result)
#         if len(str(n)[1:]) > 0:
#             sum_digits(int(str(n)[1:]), result)

def sum_digits(n):

    if n <= 9:
        return n

    last_digit = n % 10
    return sum_digits(n // 10) + last_digit


# print(sum_digits(12) == 3)
# print(sum_digits(552) == 12)
print(sum_digits(123456789))

print(sum_digits(123456789) == 45)
#
# print(sum_digits(12))
# print(sum_digits(552))
# print(sum_digits(123456789))
