
def merge(first, second):
    mix = []
    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            mix.append(first[i])
            i += 1
        else:
            mix.append(second[j])
            j += 1

    while i < len(first):
        mix.append(first[i])
        i += 1

    while j < len(second):
        mix.append(second[j])
        j += 1
        
    return mix


def merge_sort(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2
    
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


array = [5, 4, 3, 2, 1]
arr = merge_sort(array)
print(arr)