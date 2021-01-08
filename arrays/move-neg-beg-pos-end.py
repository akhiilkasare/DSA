### Move all the negative number at the beginning and positive numbers at the end


def rearrange(arr,n):

    j = 0
    for i in range(0,n):
        if arr[i] < 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j = j + 1
    print(arr)

arr = [0,3,4-1,3,6,0,2,-8,-2]
n = len(arr)
rearrange(arr, n)