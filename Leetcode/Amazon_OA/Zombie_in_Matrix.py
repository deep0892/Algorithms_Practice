# https://leetcode.com/discuss/interview-question/411357/
"""
Discription of question in above link
"""
def minHour(grid):
    if not grid:
        return -1
    rows, columns = len(grid), len(grid[0])
    if not rows and not columns:
        return -1
    
    q = [ [i,j] for i in range(rows) for j in range(columns) if grid[i][j] == 1 ]
    
    hour = -1
    direction = [[1,0], [0,1],[-1,0],[0,-1]]
    while len(q) > 0:
        size = len(q)
        for i in range(size):
            current = q.pop(0)
            for [i,j] in direction:
                ni, nj = current[0]+i, current[1]+j
                if( ni >= 0 and ni < rows and nj >= 0 and nj < columns and grid[ni][nj] == 0 ):
                    grid[ni][nj] = 1
                    q.append([ni,nj])
        hour += 1
    return hour

def main():
    grid = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1]
            ]
    print(minHour(grid))


if __name__ == "__main__":
    main()
