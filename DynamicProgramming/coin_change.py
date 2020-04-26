def count(arr,m,n):

    if(n == 0):
        return 1

    if(n < 0):
        return 0
    
    if(m <=0 and n >= 1):
        return 0
    
    return count(arr, m-1, n) + count(arr, m, n-arr[m-1])

def count_overlapping(s,m,n):
    tb = [0]*(n+1)
    tb[0] = 1
    for i in range(0,m):
        for j in range(s[i],n+1):
            tb[j] += tb[j - s[i]]
            
    return tb[n]

# Driver program to test the above function
def main(): 
    arr =  [1,2,3,5]
    m = len(arr)
    print(count(arr,m,7))
    print(count_overlapping(arr,m,7))
  
if __name__=="__main__": 
    main()
