# https://leetcode.com/discuss/interview-question/364760/
"""
Discription of question in above link
"""
def get_rank(arr,el):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] == el:
            count +=1
    return count

def max_network_rank(A, B, N):
    dic = {}
    max_net_rank = 0
    M = len(A)
    for i in range(0,M):
        cnt_a = 0
        nt_b = 0
        a = A[i]
        b = B[i]
        if a in dic:
            cnt_a = dic[a]
        else:
            cnt_a = get_rank(A,a) + get_rank(B,a)
        if b in dic:
            cnt_b = dic[a]
        else:
            cnt_b = get_rank(A,b) + get_rank(B,b)
        max_net_rank = max(max_net_rank, cnt_a + cnt_b -1)
    return max_net_rank
    
# Driver program to test the above function
def main(): 
    A = [1,2,3,4]
    B = [2,3,4,5]
    N = 5
    print(max_network_rank(A,B,N))
  
if __name__=="__main__": 
    main()
