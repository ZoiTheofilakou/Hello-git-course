input_str = input("Enter numbers, separated by ',': ")
input_list = input_str.split(",")
value_list = [int(x.strip()) for x in input_list]

print("input_list:", input_list)
print("value_list:", value_list)

# The actual merge sort logic here...

def merge_sort(array):
    if len(array) < 2:
        return array
    m = len(array) // 2
    return merge(merge_sort(array[:m]), merge_sort(array[m:]))

def merge(left, right):
    result = []
    while left and right:
        result.append((left if left[0] <= right[0] else right).pop(0))
    result.extend(left or right)
    return result

sorted_list = merge_sort(value_list)
print(sorted_list)
