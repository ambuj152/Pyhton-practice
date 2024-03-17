def move(array):
    array.sort()
    b=array[::-1]
    print(b)
    

array=[-1,-2,-5,6,7,-3,8]
move(array)

def move_negatives_to_right(array):
    result = [None] * len(array)
    left = 0

    for num in array:
        if num >= 0:
            result[left] = num
            left += 1

    for num in array:
        if num < 0:
            result[left] = num
            left += 1

    return result

array = [-1, -2, -5, 6, 7, -3, 8]
result_array = move_negatives_to_right(array)
print(result_array)
