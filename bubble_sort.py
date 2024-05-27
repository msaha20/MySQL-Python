def bubble_sort(arr):
    n = len(arr)  
    # Traverse through all array elements
    for ii in range(n):
        isSwapped = False     
        for jj in range(0, n-1-ii):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next  
            if arr[jj] > arr[jj+1]:
               arr[jj], arr[jj+1] = arr[jj+1], arr[jj]
               isSwapped = True
        if isSwapped is False:
            return arr  
        print (arr)
    return arr


if __name__ == "__main__":
      s = input("Enter numbers separated by space: ")
      nums = list(map(int, s.split()))
      sorted_array = bubble_sort(nums)
      print("Sorted Array:", sorted_array)

'''userArray = input("Enter array:").split()
    print(userArray)
    s = input()
    numbers = list(map(int, s.split()))
    ##userArray = input("Enter array:")
    userArray = bubble_sort(userArray)
    print ("Sorted Array: ", userArray) '''

                    

