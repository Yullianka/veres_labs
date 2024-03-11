def is_list_monotonic(array: list):
    is_increased = True
    is_decreased = True
    length = len(array)

    if length == 1:
        return True
    


    for i in range(length - 1):
        if array[i + 1] < array[i]:
            is_increased = False
            break

    for i in range(length - 1):
        if array[length - i - 1] > array[length - i - 2]:
            is_decreased = False
            break

    return is_decreased or is_increased