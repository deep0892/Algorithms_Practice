# https://leetcode.com/problems/hand-of-straights/
"""
Discription of question in above link
"""


def isNStraightHand(hand, W):

    if len(hand) % W != 0:
        return False

    x = {}
    for el in hand:
        if x.__contains__(el):
            x[el] += 1
        else:
            x[el] = 1

    keys = list(x.keys())
    keys.sort()

    while(keys and len(keys) > 0):
        min = keys[0]

        for i in range(min, min + W):
            if (not x.__contains__(i)):
                return False
            if x[i] == 1:
                x.pop(i)
                keys.remove(i)
            else:
                x[i] -= 1

    return True


#  Driver program to test the above function


def main():
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    W = 3
    print(isNStraightHand(hand, W))


if __name__ == "__main__":
    main()
