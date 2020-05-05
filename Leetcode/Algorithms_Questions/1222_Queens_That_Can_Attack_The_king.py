# https://leetcode.com/problems/queens-that-can-attack-the-king/
"""
Discription of question in above link
"""


def queensAttacktheKing(queens, king):
    result = []
    seen = [[False for i in range(0, 9)] for i in range(0, 9)]
    for queen in queens:
        seen[queen[0]][queen[1]] = True
    directions = {-1, 0, 1}
    for dx in directions:
        for dy in directions:
            if dx == 0 and dy == 0:
                continue
            x = king[0]
            y = king[1]
            while(x + dx >= 0 and x + dx < 8 and y + dy >= 0 and y+dy < 8):
                x += dx
                y += dy
                if seen[x][y]:
                    result.append([x, y])
                    break
    return result


#  Driver program to test the above function


def main():
    queens = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
    king = [0, 0]
    print(queensAttacktheKing(queens, king))


if __name__ == "__main__":
    main()
