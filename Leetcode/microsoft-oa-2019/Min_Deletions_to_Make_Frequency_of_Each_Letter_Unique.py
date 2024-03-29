# https://leetcode.com/discuss/interview-question/398035/
"""
Discription of question in above link
"""
from collections import defaultdict
from typing import Dict, List, Set


def minDeletions(input: str) -> int:
    if len(input) == 0 or len(input) == 1:
        return 0

    result: int = 0
    char_count: Dict[str, int] = defaultdict(int)
    char_set: Set = set()
    for c in input:
        char_count[c] = char_count[c] + 1

    for k, e in char_count.items():
        if e in char_set:
            for i in range(e, 0, -1):
                if i not in char_set:
                    char_set.update([i])
                    break
                result += 1
        else:
            char_set.update([e])
    return result

# Alternate solution:
def minDeletions_alt(self, s: str) -> int:
    freq = {}
    count_arr = []
    num_del = 0
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for item,count in freq.items():
        if count in count_arr:
            while count in count_arr and count>0:
                count -=1
                num_del += 1
        count_arr.append(count)

    return num_del

# Driver program to test the above function


def main():
    print(minDeletions("aabbffddeaee"))
    print(minDeletions("eeeeffff"))
    print(minDeletions("example"))
    print(minDeletions(""))


if __name__ == "__main__":
    main()
