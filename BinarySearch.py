def binarySearch(li,x):
    low=0
    high=len(li)-1

    while low <= high:
        mid = (low + high) // 2
        if li[mid] == x:
            return mid
        elif li[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
            
    return f"This number {x} is not included."

        