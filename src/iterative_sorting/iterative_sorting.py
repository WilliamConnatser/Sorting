# Selection Sort
# O(n^2) comparisons, O(n) swaps
# Stable Sort
# Type: Selection Sort
def selection_sort( arr ):

    # loop through n-1 elements
    for i in range(0, len(arr) - 1):

        # Find next smallest element
        smallest_index = i
        for x in range(i+1,len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x

        #Easier to read but less efficient.
        #Searches unsorted list twice first to find min value
        #Then again in order to find the index
        '''
        #Get smallest index of unsorted list
        unsorted_list = arr[i:]
        smallest_index = arr.index(min(unsorted_list))
        '''
        
        # Swap min value to current index
        arr[i],arr[smallest_index] = arr[smallest_index],arr[i]

    return arr


# Bubble Sort
# O(n^2) Comparison, O(n^2) Swaps
# Stable Sort
# Type: Exchange Sort
def bubble_sort( arr ):
    #Starting from the first array element
    #For each item in the array minus one
    x = 0
    while x < len(arr)-1:
        #Starting from the first array element
        #For each array element that is unsorted
        #The amount of unsorted elements gets smaller each time the outer while loop finishes
        y = 0
        while y < len(arr)-x-1:
            if arr[y+1] < arr[y]:
                #If the next array element is smaller than the current element
                #Then swap them and reset index to 0
                arr[y],arr[y+1] = arr[y+1], arr[y]
            #Increment j
            y += 1
        #Increment i
        x += 1
    return arr

# Count Sort
# O(n+k) where k is the range of the non-negative key values
# Stable Sort
# Type: Distribution Sort
def count_sort( arr, maximum=-1 ):
    #Make a list that stores the number of times each integer occurs
    #Compute the cumulative total of matches from starting at index 0
    return arr