def insertion_sort(array):
    for i in range(0, len(array)-1):
        j = i + 1
        while j > 0:
            if array[j] < array[j-1]:
                temp = array[j-1]
                array[j-1] = array[j]
                array[j] = temp
            else:
                break
            j -= 1


array = [5, 3, 4, 1, 2, 0]
insertion_sort(array)
print(array)
