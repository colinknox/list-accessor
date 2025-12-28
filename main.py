#!/usr/bin/python3

# list = [1, 2, 3, 4, 5, 6]
# list = [5, 10, 15, 20, 25, 30, 35, 40, 45]
list = [6, 7, 8, 9, 10, 11]

def get_first(items):
    return items[0]

def get_last(items):
    return items[-1]

def get_middle(items):
    list_length = len(items)
    ceiling = list_length // 2

    if list_length % 2 == 1:
        return items[ceiling]
    else:
        return items[(int(list_length / 2)) - 1]

def get_at_index(items, index):
    return items[index]

def get_first_three(items):
    return items[0:3]


test1 = get_at_index(list, 5)
test1 = get_first_three(list)


# test1 = get_first(list)
# test1 = get_last(list)
# test1 = get_middle(list)

print(test1)