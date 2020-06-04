# https://leetcode.com/discuss/interview-question/398031/
# https://leetcode.com/discuss/interview-question/398037/
"""
Discription of question in above link
"""

def validLongestSubstring(input: str) -> str:
    str_start: int = 0
    end: int = 1
    max_length: int = 1
    max_start: int = 0
    first: str = input[0]
    cnt: int = 1
    flag: int = 1
    while(end < len(input)):
        if input[end] == first and cnt >= 2:
            flag = 0
            if(max_length < end - str_start):
                max_start = str_start
                max_length = end - str_start
            str_start = end - 1
            first = input[str_start]
            cnt = 1
        elif input[end] != first:
            first= input[end]
            end +=1
            cnt = 1
        else:
            cnt +=1
            end +=1
    if flag ==1: 
        return input  
    return input[max_start: max_start+max_length]

# Driver program to test the above function
def main(): 
    print(validLongestSubstring("aabbaaaaabb")) # expected: aabbaa
    print(validLongestSubstring("aabbaabbaabbaa"))  # expected: aabbaabbaabbaa
    print(validLongestSubstring("abbaabbaaabbaaa"))  # expected: abbaabbaa

if __name__=="__main__": 
    main()
