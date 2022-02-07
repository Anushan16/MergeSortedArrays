#given two separate sorted arrays, return a sotrted array
# [0,3,4,31] [4,6,40]

# initalize a empty array to hold the new sorted string 

def newSortedArray(arr1,arr2):
  sortedArray = []

#setup a pointer for arr 1

  pointer1 = 0

#setup a pointer for arr 2

  pointer2 = 0 

# create a while loop to run until the length of the new array is less than length of array1 + array 2
  while (pointer2 < len(arr2)) and (pointer1 < len(arr1)):
    print(sortedArray)
    print(f'length of the arr1 is {len(arr1)} and the current pointer is {pointer1}')    
    print(f'length of the arr2 is {len(arr2)} and the current pointer is {pointer2}')
#use pointers as index and compare the elements at arr[pointer] if the arr is smaller , increasce that specific pointer by one and leave the other
    if arr1[pointer1] <= arr2[pointer2]:
      sortedArray.append(arr1[pointer1])
      print(f'{arr1[pointer1]} has been added to sortedArray')
      pointer1 +=1
      
      
      
      
    elif arr2[pointer2] <arr1[pointer1]:
      sortedArray.append(arr2[pointer2])
      print(f'{arr2[pointer2]} has been added to sortedArray')
      pointer2 +=1
      
    #merge the contents of all three lists if there are any items remaining after termination of while loop
  return sortedArray + arr1[pointer1:]+arr2[pointer2:]

print(newSortedArray([0,3,4,31],[4,6,40]))








