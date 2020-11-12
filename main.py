
grid =[[8, 1, 0, 0, 3, 0, 0, 2, 7], 
        [0, 6, 2, 0, 5, 0, 0, 9, 0], 
        [0, 7, 0, 0, 0, 0, 0, 0, 0], 
        [0, 9, 0, 6, 0, 0, 1, 0, 0], 
        [1, 0, 0, 0, 2, 0, 0, 0, 4], 
        [0, 0, 8, 0, 0, 5, 0, 7, 0], 
        [0, 0, 0, 0, 0, 0, 0, 8, 0], 
        [0, 2, 0, 0, 1, 0, 7, 5, 0], 
        [3, 8, 0, 0, 7, 0, 0, 4, 2]]

def print_board(board):
    for i in range(9):
        line = " "
        if i%3 == 0 and i!=0:
            print("--------------------")
            
        for j in range(9):
            if j%3 == 0 and j!=0:
                line += "|"
            line = line + str(board[i][j])+ " "
        print(line)

def posiibility(x,y,n):
    global grid
    for i in range(0,9):
        if grid[x][i] == n:
            return False
    for i in range(0,9):
        if grid[i][y] == n:
            return False
    a = (x//3)*3
    b = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[a+i][b+j] == n:
                return False
    return True
def empty_box():

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i,j
    return None           
def solve():
    find  = empty_box()
    if not find:
        return True
    else:
        x,y = find

    for n in range(1,10):
        if posiibility(x,y,n):
            grid[x][y] = n

            if solve():
                return True

            grid[x][y] = 0
    return False
print("This the board I need to solve where 0 represents empty box ")                  
print_board(grid)
solve() 
print("")
print("The final solution to this sudoko board ")
print_board(grid)              
