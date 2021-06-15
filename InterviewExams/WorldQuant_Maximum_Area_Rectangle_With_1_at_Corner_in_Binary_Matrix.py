# A brute force approach based Python3 program to
# find if there is a rectangle with 1 as corners.
 
def maxRectangle(m):
    max_rectangle = 0
    # finding row and column size
    rows = len(m)
    if (rows == 0):
        return False
    columns = len(m[0])
 
    # scanning the matrix
    for y1 in range(rows):
 
        for x1 in range(columns):
 
            # if any index found 1 then
            # try for all rectangles
            if (m[y1][x1] == 1):
                for y2 in range(y1 + 1, rows):
                    for x2 in range(x1 + 1, columns):
                        if (m[y1][x2] == 1 and
                            m[y2][x1] == 1 and
                            m[y2][x2] == 1 ):
                            print(x1,x2,y1,y2)
                            max_rectangle = max(max_rectangle, (x2-x1)*(y2-y1))
    return max_rectangle
 
# Driver code
mat = [[1, 0, 0, 1, 0],
       [1, 0, 1, 0, 1],
       [1, 0, 0, 1, 1],
       [1, 0, 1, 0, 1]]
 
print(maxRectangle(mat))