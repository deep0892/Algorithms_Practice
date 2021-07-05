# https://leetcode.com/problems/partition-labels/
"""
Discription of question in above link
"""

from typing import List
import operator


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_occur = {item: index for index, item in enumerate(S)}

        flag, current, result = 0, 0, []
        for index, item in enumerate(S):
            current = max(current, last_occur[item])
            if(current == index):
                result.append(current - flag + 1)
                flag = index + 1

        return result


def main():
    S = "ababcbacadefegdehijhklij"
    sol = Solution()
    print(sol.partitionLabels(S))


if __name__ == "__main__":
    main()
