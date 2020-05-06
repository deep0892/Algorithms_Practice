# https://leetcode.com/problems/task-scheduler/
"""
Discription of question in above link
"""


def leastInterval(tasks, n):
    char_map = [0] * 26
    for el in tasks:
        char_map[ord(el)-ord('A')] += 1
    char_map.sort()
    max_val = char_map[25] - 1
    idle_slots = max_val * n

    for i in range(24, -1, -1):
        idle_slots -= min(char_map[i], max_val)

    return len(tasks) + idle_slots if idle_slots > 0 else len(tasks)


#  Driver program to test the above function


def main():
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(leastInterval(tasks, n))


if __name__ == "__main__":
    main()
