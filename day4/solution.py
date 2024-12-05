# DFS in all directions from every X found until condition is not met
def xmas_dfs(r, c, matrix):
    rows, cols = range(len(matrix)), range(len(matrix[0]))
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1], 
                 [1, 1], [1, -1], [-1, 1], [-1, -1]]

    # For each direction, if 3 cells in that direction, check if they meet MAS condition
    count = 0
    for dx, dy in directions:
        if r + 3*dx in rows and c + 3*dy in cols:
            mr, mc = r + dx, c + dy # Checks the expected 'M' and so on
            ar, ac = r + 2*dx, c + 2*dy
            sr, sc = r + 3*dx, c + 3*dy
            if matrix[mr][mc] == 'M' and matrix[ar][ac] == 'A' and matrix[sr][sc] == 'S':
                count += 1
    return count

def cross_mas_dfs(r, c, matrix):
    rows, cols = range(len(matrix)), range(len(matrix[0]))
    diag1 = [[1, 1], [-1, -1]]
    diag2 = [[1, -1], [-1, 1]]

    # Add the diagonal chars to sets and check if they meet the M,S conditon
    diag1set = set()
    diag2set = set()
    for dx, dy in diag1:
        if r+dx not in rows or c+dy not in cols:
            return False

        diag1set.add(matrix[r+dx][c+dy]) 
    for dx, dy in diag2:
        if r+dx not in rows or c+dy not in cols:
            return False

        diag2set.add(matrix[r+dx][c+dy]) 

    # If both sets have M and S, it is valid
    if diag1set == {'M', 'S'} and diag2set == {'M', 'S'}:
        return True
    return False

# Handle and preprocess input into 2d matrix
with open('input.txt', 'r') as file:
    chars = []
    for line in file:
        chars.append(list(line))
    xmas_count = 0 
    cross_mas_count = 0 
    for i in range(len(chars)):
        for j in range(len(chars[0])):
            if chars[i][j] == 'X':
                xmas_count += xmas_dfs(i, j, chars)
            if chars[i][j] == 'A':
                cross_mas_count += 1 if cross_mas_dfs(i, j, chars) else 0
    print('Cross XMAS Count: ', cross_mas_count)
    print('Xmas Count: ', xmas_count)