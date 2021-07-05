# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
"""
Discription of question in above link
"""


def removeDuplicates(S):
    if(len(S) == 0 or len(S) == 1):
        return S
    x = []
    for j in S:
        if(x and j == x[-1]):
            x.pop()
        else:
            x.append(j)
    return ''.join(x)

#  Driver program to test the above function


def main():
    source = "abbaca"
    print(removeDuplicates(source))


if __name__ == "__main__":
    main()
