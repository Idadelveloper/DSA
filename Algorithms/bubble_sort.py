def bubble_sort(array):
    # run the steps n-1 times
    for i in range(len(array)):
        swapped = False
        # for each step, max item will come at the last respective index
        for j in range(len(array) - 1):
            # swap if the item is smaller than previous item
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
                swapped = True

        if not swapped:
            break
            
