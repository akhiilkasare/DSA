### Cyclically rotate an array by one

def rotate(arr, n):

    ###storing the last element of an array
    x = arr[n - 1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = x

arr = [1,2,3,4,5]
n = len(arr)

print("The Given array is : ", arr)
for i in range(0, n):
    print(arr[i], end=' ')

rotate(arr,n)

print("\nThe Rotated array is :")
for i in range(0, n):
    print(arr[i], end=' ')
