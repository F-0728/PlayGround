import turtle
maze = []
with open('maze.txt', 'r') as file:
    for line in file:
        maze.append(line)

turtle.tracer(0)
H = len(maze)
W = len(maze[0])
sx = 0
sy = 0
gx = 0
gy = 0

t = turtle.Turtle()
t.ht()
t.pu()
t.setx(0)
t.sety(0)
t.pd()

def wall_make(y, x):
    x *= 10
    y *= -10
    t = turtle.Turtle()
    t.ht()
    t.color("black")
    t.pu()
    t.setx(x)
    t.sety(y)
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.forward(10)
        t.right(90)
        t.forward(10)
        t.right(90)
    t.end_fill()
    
def goal_make(y, x):
    x *= 10
    y *= -10
    t = turtle.Turtle()
    t.ht()
    t.color("red")
    t.pu()
    t.setx(x)
    t.sety(y)
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.forward(10)
        t.right(90)
        t.forward(10)
        t.right(90)
    t.end_fill()
    
start_x = 0
start_y = 0

for i in range(H):
    for j in range(W):
        if maze[i][j] == '+':
            t.pd()
            wall_make(i, j)
            t.pu()
        elif maze[i][j] == '*':
            gx = i
            gy = j
            goal_make(i, j)
        elif maze[i][j] == 'T':
            sx = i
            sy = j
            start_x = i * 10
            start_y = j * -10
            start_x += 5
            start_y -= 5

turtle.tracer(1) 
t0 = turtle.Turtle()
t0.color("green")
t0.pu()
t0.goto(start_x,start_y)
t0.pd()

already = [[False] * W for i in range(H)]
route = []

def chk_r(i, j):
    if maze[i + 1][j] == '+':
        return False
    elif already[i + 1][j] == True:
        return False
    else:
        return True 
def chk_l(i, j):
    if maze[i - 1][j] == '+':
        return False
    elif already[i - 1][j] == True:
        return False
    else:
        return True   
def chk_u(i, j):
    if maze[i][j + 1] == '+':
        return False
    elif already[i][j + 1] == True:
        return False
    else:
        return True    
def chk_d(i, j):
    if maze[i][j - 1] == '+':
        return False
    elif already[i][j - 1] == True:
        return False
    else:
        return True
 
def routing(i, j):
    if i < 0 or i >= H or j < 0 or j >= W:
        return False
    already[i][j] = True
    if i == gx and j == gy:
        return True
    if chk_r(i, j):
        if routing(i + 1, j):
            route.append([i+1,j])
            return True
    if chk_l(i, j):
        if routing(i - 1, j):
            route.append([i-1,j])
            return True
    if chk_u(i, j):
        if routing(i, j + 1):
            route.append([i,j+1])
            return True
    if chk_d(i, j):
        if routing(i, j - 1):
            route.append([i,j-1])
            return True
    return False

routing(sx,sy)
 
route.reverse()
print(route)

for i in range(len(route)):
    t0.goto(10*route[i][1]+5, -10*route[i][0]-5)

turtle.done()