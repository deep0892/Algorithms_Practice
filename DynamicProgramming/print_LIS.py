def printLIS(arr: list):
    for x in arr:
        print(x, end=" ")
    print()
 

def constructPrintLIS(arr: list, n: int):

    l = [[] for i in range(n)]
 
    l[0].append(arr[0])
 
    for i in range(1, n):

        for j in range(i):
            if arr[i] > arr[j] and (len(l[i]) < len(l[j]) + 1):
                l[i] = l[j].copy()
        l[i].append(arr[i])
 
    maxx = l[0]

    for x in l:
        if len(x) > len(maxx):
            maxx = x

    printLIS(maxx)
 
# Driver Code
if __name__ == "__main__":
 
    arr = [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ]
    n = len(arr)
 
    # construct and print LIS of arr
    constructPrintLIS(arr, n)