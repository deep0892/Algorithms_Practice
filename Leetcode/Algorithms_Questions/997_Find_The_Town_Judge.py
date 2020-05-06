# https://leetcode.com/problems/find-the-town-judge/
"""
Discription of question in above link
"""


def findJudge(N, trust):
    count = [0 for i in range(0, N+1)]
    for item in trust:
        count[item[0]] -= 1
        count[item[1]] += 1
    for i in range(1, N+1):
        if(count[i] == N-1):
            return i
    return -1


def main():
    trust = [[1, 2]]
    N = 2
    print(findJudge(N, trust))


if __name__ == "__main__":
    main()
