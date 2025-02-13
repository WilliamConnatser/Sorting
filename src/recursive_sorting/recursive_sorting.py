#Merge Sort Helper
def merge( left, right ):
    # Make empty list to store the result
    result = []
    # While both lists have at least one item
    while len(left) and len(right):
        if left[0] < right[0]:
            # If the first item on the left is smaller than the first on the right
            # Then append it to the result and remove it from the left
            result.append(left[0])
            left = left[1:]
        else:
            # Else the first item on the right is smaller than the first on the left
            # So append it to the result and remove it from the right
            result.append(right[0])
            right = right[1:]

    # If there is 1 item left in the left or right
    # Then append their values to the result
    return  result + left + right

# Merge Sort Main
# O(n log(n))
# One of the better sorting runtimes out there
# Many native sort() functions use Merge Sort
def merge_sort( arr ):

    #If arr length is 1 or less
    # Then return array as-is
    if len(arr) <= 1:
        return arr
    
    #Get middle index
    middle = len(arr) // 2
    
    #Else split the array into two on the middle index
    #Recursively call merge_sort until 
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    
    #If the last array item on the left is smaller than the first array item on the left
    #Then combine them and return it.. they are in order
    if left[-1] < right[0]:
        return left + right
    
    #Else return the merged arrays bc there's more sorting to do
    return merge(left,right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, left, middle, right):
    result = []
    while left < middle and right > middle:
        if arr[left] < arr[middle]:
            result.append(arr[left])
            left += 1;
        else:
            result.append(arr[middle])
            middle += 1;
    
    result = result + arr[left:middle-1] + arr[middle:right]
    print(f"result from merge: {result}")
    return result

def merge_sort_in_place(arr, left, right):
    print(f"Sort Array: {arr} L: {left} R: {right}")
    if left >= right:
        return arr
    
    middle = (right + left) // 2
    merge_sort_in_place(arr, left, middle)
    merge_sort_in_place(arr, middle, right)

    if arr[middle-1] < arr[middle]:
        return arr;

    return merge_in_place(arr,left,middle,right)


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


#Quick Sort
# O(n2)
'''While Quick Sort has "quick" in its name,
it is typically not used as frequently as Merge Sort.
Although it is quick in a best case scenario,
worst case for Quick Sort is very bad.
Because of this, it is not often chosen for production.'''
def partition(arr):
    left = []
    pivot = arr[0]  # or make random
    right = []
    for v in arr[1:]:
        if v < pivot:
            left.append(v)
        else:
            right.append(v)
    return left, pivot, right

def quicksort(arr):
    if arr == []:
        return []
    left, pivot, right = partition(l)
    return quicksort(left) + [pivot] + quicksort(right)