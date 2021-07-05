# https://leetcode.com/problems/reorder-data-in-log-files/
"""
Discription of question in above link
"""

from typing import List
import operator


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        result = []
        letterLog = []
        digitLog = []

        for log in logs:
            splitLog = log.split(" ")
            if splitLog[1].isdigit():
                digitLog.append(log)
            else:
                letterLog.append([splitLog[0], " ".join(splitLog[1:])])

        for i in sorted(letterLog, key=operator.itemgetter(1, 0)):
            result.append(" ".join(i))
        return result + digitLog


def main():
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
            "let2 own kit dig", "let3 art zero"]
    sol = Solution()
    print(sol.reorderLogFiles(logs))


if __name__ == "__main__":
    main()
