def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greather = [i for i in array[1:] if i >= pivot]
        return quicksort(less) + [pivot] + quicksort(greather)


print(quicksort([10, 5, 2, 3]))
