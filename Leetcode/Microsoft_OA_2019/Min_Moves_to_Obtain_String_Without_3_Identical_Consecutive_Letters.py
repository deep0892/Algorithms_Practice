# https://leetcode.com/discuss/interview-question/365872/
"""

"""
def count(arr):
    m = len(arr)
    i = 0 
    cnt = 0
    
    while(i < m-2):
        if(arr[i] == arr[i+1] and arr[i] == arr[i+2]):
            cnt += 1
            i += 3
        else:
            i += 1
    return cnt
    
    
# Driver program to test the above function
def main(): 
    print(count("baabab"))
    assert count("baaaaa"), 1
    assert count("baaaaaa"), 2
    assert count("baaaab"), 1
    assert count("baaabbaabbba"), 2
    assert count("baabab"), 0
    assert count("bbaabbaabbabab"), 0
  
if __name__=="__main__": 
    main()
