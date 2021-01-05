### Find the smallest element

def kthSmallest(arr, n, k):

    ##Sorting the array
    arr.sort()

    return arr[k-1]

if __name__ == "__main__":

    arr = [1,54,6,8]
    n = len(arr)
    k = 2
    print("The kth smallest elenent is : ", kthSmallest(arr, n, k))