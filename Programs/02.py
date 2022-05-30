def order(array):
    # Return false if array is not of propper length
    if len(array) < 2:
        return(False)

    # Assume list is ascending if True
    if array[0] < array[1]:
        # Loop through the list, excluding pos 0
        for i in range(1, len(array)):
            # return ascending if loop meets the end
            if i+1 == len(array):
                return 'ascending'
            # Check order, if wrong return neither
            if array[i-1] > array[i]:
                return 'neither'

    # Assume list is descending
    else:
        # Loop through the list, excluding pos 0
        for i in range(1, len(array)):
            # return descending if loop meets the end
            if i+1 == len(array):
                return 'descending'
            # Check order, if wrong return neither
            if array[i-1] < array[i]:
                return 'neither'

print(order([1,5,8,10]))        # ascending
print(order([50,30,20,5]))      # descending
print(order([50,100,60,20]))    # neither
print(order([0]))               # False