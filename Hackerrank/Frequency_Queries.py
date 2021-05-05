# https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps&isFullScreen=true
"""
"""

from typing import List

class Solution:
    def freqQuery(self, queries):
        freq = {}
        res = []
        if(len(queries) == 0 ):
            return []
        
        for item in queries:
            flag = 0
            if item[0] == 1:
                freq[item[1]] = freq.get(item[1],0) + 1
            elif item[0] == 2 & freq.get(item[1],0) > 0:
                freq[item[1]] = freq.get(item[1],0) - 1
            elif item[0] == 3:
                keys = freq.keys()
                for key in keys:
                    if freq[key] == item[1]:
                        flag = 1
                res.append(flag)
                
        return res


def main():
    queries = [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
    sol = Solution()
    print(sol.freqQuery(queries))


if __name__ == "__main__":
    main()
