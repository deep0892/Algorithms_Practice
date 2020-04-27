# https://leetcode.com/discuss/interview-question/366869/
"""
Discription of question in above link
"""

def getSmallString(input: str) -> str:
    result: str = input 
    if len(input) == 0 or len(input) == 1:
        return input
    for i in range(0, len(input)-1):
        if input[i] > input[i+1]:
            result = input[0:i] + input[i+1 : len(input)]
            break
    return result

# Driver program to test the above function
def main():
    print(getSmallString("zyxwvu"))
    print(getSmallString("abczd"))
    print(getSmallString("abcde"))

if __name__=="__main__": 
    main()
