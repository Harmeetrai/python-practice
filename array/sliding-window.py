print("Sliding Windows Algorithm")
print("-------------------------")

# Sliding Window Algorithm finding 
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Array: ", array)

def fixedSlidingWindow():
    # sum of elements when subarray size is 3
    subarraySize = 3
    print("Subarray Sum Size: ", subarraySize)

    subArray = sum(array[:subarraySize])
    result = [subArray]

    for i in range(1,len(array)-subarraySize+1):
        subArray = subArray - array[i-1]
        subArray = subArray + array[i+subarraySize-1]
        result.append(subArray)

    return result
    
# Example: finding minimal size subarray that is equal to or greater than value
def dynamicSlidingWindow(sum):
    min_length = float('inf')
    
    start,end,current_sum = 0,0,0

    while end < len(array):
        current_sum = current_sum + array[end]
        end += 1

        while start < end and current_sum >= sum:
            current_sum -= array[start]
            start += 1
            min_length = min(min_length, end-start+1)
    return min_length

print("Starting fixed sliding window with subarray size 3")
print(fixedSlidingWindow())
print("Starting dynamic sliding window with sum = 12")
print(dynamicSlidingWindow(12))