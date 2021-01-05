## Find the k largest element in an array

def kLargest(arr, k):

    ##Sorting the array
    arr.sort(reverse=True)

    for i in range(k):
        print(arr[i], end=' ')

arr = [12,20,30,40,50]

k = 3

kLargest(arr, k)