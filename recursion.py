def sum_to_one(n):
    if n == 1:
        return 1
    else:
        return n + sum_to_one(n-1)


print(sum_to_one(4))
