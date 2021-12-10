def getMaxIndex(array, start, end):
    maximum = start

    for i in range(start, end+1):
        if array[maximum] < array[i]:
            maximum = i

    return maximum


def swap(array, first, second):
    temp = array[first]
    array[first] = array[second]
    array[second] = temp


def selection_sort(array):
    for i in range(len(array)):
        last = len(array) - i - 1
        maxIndex = getMaxIndex(array, 0, last)

        swap(array, maxIndex, last)


array = [5, 3, 4, 1, 2, 0]
selection_sort(array)
print(array)
