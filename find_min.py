def find_min(my_list):
    if len(my_list) == 0:
        return None
    if len(my_list) == 1:
        return my_list[0]
    popped = my_list.pop()
    return min(find_min(my_list), popped)

print(find_min([42, 17, 2, -1, 67]))
print(find_min([]))
print(find_min([13, 72, 19, 5, 86]))