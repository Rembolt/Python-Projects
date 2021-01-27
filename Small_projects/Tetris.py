#parei aquipppppppppppppppppp
#tenho que ajustar o fato de ele poder mover em certas condicoes erradasppppppppppppppppp
#testar ate funcionar como estappppppppppppppppp
#mudar condicao de mover pra esquerda e direitapppppppppppppppp
#adicionar rotacaoppppppppppppppppppp
#testar tudopppppppppppppppppppppppp
#adicionar condicao de rotacaopppppppppppppppppppppppp
#adicionar toques finais/score/desaparece quando entra na peca de baixo/botoes pra girar 180,pra um lado e pro outroppppppppppppppppppppppppppppppppp
#Num futuro, adicionar espera pra decer, hold de pecas, decser aotomatico, mostrar proximas pecas, otimizar logica do jogo e descer devagar
import turtle
import time
import random
 
wn = turtle.Screen()
wn.title ("TETRIS")
wn.bgcolor("Black")
wn.setup(width =600,height =700)
wn.tracer(0)

last_shape = None

class Shape():
    def __init__(self, last_shape):
        self.color = None
        self.x = 4
        self.y = 0 
        self.shape = []
        shape_type = random.randint(0,6)
        if last_shape == shape_type:   
            shape_type = random.randint(0,6) 
        if last_shape == shape_type:   
            shape_type = random.randint(0,6) 

        if shape_type == 0:
                square = [[1,1],
                          [1,1]]
                self.color = 3
                self.shape.extend(square)
        elif shape_type == 1:
                line = [[1],
                        [1],
                        [1],
                        [1]]
                self.color = 5
                self.shape.extend(line)
        elif shape_type == 2:
                right_L = [[1,0],
                           [1,0],
                           [1,1]]
                        
                self.color = 2
                self.shape.extend(right_L)
        elif shape_type == 3:
                left_L = [[0,1],
                          [0,1],
                          [1,1]]
                self.color = 6
                self.shape.extend(left_L)
        elif shape_type == 4:
                t = [[0,1,0],
                     [1,1,1]]
                self.color = 7
                self.shape.extend(t)
        elif shape_type == 5:
                right_z = [[1,0],
                           [1,1],
                           [0,1]]
                        
                self.color = 4
                self.shape.extend(right_z)
        elif shape_type == 6:
                left_z = [[0,1],
                          [1,1],
                          [1,0]]
                self.color = 1
                self.shape.extend(left_z)
        
        last_shape = shape_type
        self.height = len(self.shape)
        self.width = len(self.shape[0])
        
    def move_left(self, grid):
        p_locations = []
        can_move = True
        if self.x > 0:
            for y in range (self.height):
                for x in range (self.width):
                    if(self.shape[y][x] == 1):
                        p_locations.append([self.y + y,self.x + x])
                        #print(p_locations)
            for y in range (self.height):
                for x in range (self.width):
                    if(self.shape[y][x] == 1):
                        last = True
                        for c in range (len(p_locations)):
                            if p_locations[c][0] == self.y + y:
                                if p_locations[c][1] <= self.x + x - 1:
                                    last = False
                                    break                                    
                            else: 
                                continue
                    
                        if last == True:
                            if grid[self.y + y ][self.x + x - 1] != 0:
                                can_move = False 
                                #print("stop")
                                #print(self.y + y + 1,self.x + x)
                                #print(grid[self.y + y + 1][self.x + x])
                                break

            if can_move == True:
                self.erase_shape(grid)
                self.x -= 1
                self.draw_shape(grid)
            
    def move_right(self, grid):
        p_locations = []
        can_move = True
        if self.x < 10 - self.width:
            for y in range (self.height):
                for x in range (self.width):
                    if(self.shape[y][x] == 1):
                        p_locations.append([self.y + y,self.x + x])
                        #print(p_locations)
            for y in range (self.height):
                for x in range (self.width):
                    if(self.shape[y][x] == 1):
                        last = True
                        for c in range (len(p_locations)):
                            if p_locations[c][0] == self.y + y:
                                if p_locations[c][1] >= self.x + x + 1:
                                    last = False
                                    break                                    
                            else: 
                                continue
                    
                        if last == True:
                            if grid[self.y + y ][self.x + x + 1] != 0:
                                can_move = False 
                                #print("stop")
                                #print(self.y + y + 1,self.x + x)
                                #print(grid[self.y + y + 1][self.x + x])
                                break

            if can_move == True:
                self.erase_shape(grid)
                self.x += 1
                self.draw_shape(grid)

#Make this

    def set_piece(self, grid):
        self.erase_shape(grid)
        p_locations = []
        lowest = 50
        for y in range (self.height):
            for x in range (self.width):
                if(self.shape[y][x] == 1):
                    p_locations.append([self.y + y,self.x + x])
                    #print(p_locations)
        for y in range (self.height):
            for x in range (self.width):
                if(self.shape[y][x] == 1):
                    last = True
                    for c in range (len(p_locations)):
                        if p_locations[c][1] == self.x + x:
                            if p_locations[c][0] >= self.y + y + 1:
                                last = False
                                break                                    
                        else: 
                            continue
                    
                    if last == True:
                        falling = True
                        t = self.y + y
                        while falling:
                            if t == 19:
                                if lowest > t - y:
                                    lowest = t - y
                                falling = False
                            elif grid[t + 1][self.x + x] == 0:
                                t += 1
                            else:
                                if lowest > t - y:
                                    lowest = t - y
                                falling = False

        self.y = lowest
        self.draw_shape(grid)
                    

    #def move_down(self, grid):
     #   if (time.time() - old_time) < .5:
      #      self.falling = True
       #     if self.can_move(grid):
        #        self.y += 1

    def draw_shape(self, grid):
        for y in range (self.height):
            for x in range (self.width):
                if(self.shape[y][x] == 1):
                    grid[self.y + y][self.x + x] = self.color
                 
    def erase_shape(self, grid):
        for y in range (self.height):
            for x in range (self.width):
                if(self.shape[y][x] == 1):
                    grid[self.y + y][self.x + x] = 0

    def can_move(self, grid):
        p_locations = []
        can_move = True
        
        for y in range (self.height):
            for x in range (self.width):
                if(self.shape[y][x] == 1):
                    p_locations.append([self.y + y,self.x + x])
                    #print(p_locations)
        for y in range (self.height):
            for x in range (self.width):
                if(self.shape[y][x] == 1):
                    last = True
                    for c in range (len(p_locations)):
                        if p_locations[c][1] == self.x + x:
                            if p_locations[c][0] >= self.y + y + 1:
                                last = False
                                break                                    
                        else: 
                            continue
                    
                    if last == True:
                        if grid[self.y + y + 1][self.x + x] != 0:
                            can_move = False 
                            #print("stop")
                            #print(self.y + y + 1,self.x + x)
                            #print(grid[self.y + y + 1][self.x + x])
                            break
                                       
        return can_move

    def rotate_left(self, grid):
        self.erase_shape(grid)
        rotated_shape = []  

        for x in range(self.width):
            new_row = []
            for y in range(self.height -1, -1, -1):
                new_row.append(self.shape[y][x])
            rotated_shape.append(new_row)

        if self.x <= 10 - len(rotated_shape[0]):  
            
            p_locations = []
            for y in range (len(rotated_shape)):
                for x in range (len(rotated_shape[0])):
                    if rotated_shape[y][x] == 1:
                        p_locations.append([self.y + y,self.x + x])
                        #print(p_locations)
        
            can_rotate = True
            for c in range (len(p_locations)):
                if grid[p_locations[c][0]][p_locations[c][1]] != 0: 
                    can_rotate = False   

            if can_rotate == True:
                self.shape = rotated_shape
                self.height = len(self.shape)
                self.width = len(self.shape[0])
                self.draw_shape(grid)

    def rotate_right(self, grid):
        self.erase_shape(grid)
        rotated_shape = []  

        for x in range(self.width -1, -1, -1):
            new_row = []
            for y in range(self.height):
                new_row.append(self.shape[y][x])
            rotated_shape.append(new_row)

        if self.x <= 10 - len(rotated_shape[0]):  
            
            p_locations = []
            for y in range (len(rotated_shape)):
                for x in range (len(rotated_shape[0])):
                    if rotated_shape[y][x] == 1:
                        p_locations.append([self.y + y,self.x + x])
                        #print(p_locations)
        
            can_rotate = True
            for c in range (len(p_locations)):
                if grid[p_locations[c][0]][p_locations[c][1]] != 0: 
                    can_rotate = False   

            if can_rotate == True:
                self.shape = rotated_shape
                self.height = len(self.shape)
                self.width = len(self.shape[0])
                self.draw_shape(grid)
                
    def rotate_180(self, grid):
        self.rotate_right(grid)
        self.rotate_right(grid)

                
        

grid = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.turtlesize(1.15)
pen.setundobuffer(None)

def draw_grid(pen, grid):
    pen.clear()
    top= 250
    left= -110

    colors =  ["#404040", "#C70039", "#FF5733", "#FFC300", "#DAF7A6", "lightblue", "#3498DB", "#AF7AC5"]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = left + x * 25
            screen_y = top - y * 25
            color = colors[grid[y][x]]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()

def check_grid(grid):
    y = 19
    while y > 0:
        is_full = True
        for x in range(0, 10):
            if grid[y][x] == 0:
                is_full = False
                y-= 1
                break
        if is_full:
            global score
            score += 1
            draw_score(pen, score)
            for copy_y in range (y, 0, -1):
                for copy_x in range (0, 10):
                    grid[copy_y][copy_x] = grid[copy_y-1][copy_x]

def draw_score(pen, score):
    pen.color("#404040")
    pen.hideturtle()
    pen.goto(-110, 270)
    pen.write("Score:  {}".format(score), move=False, align="left", font= ("Arial", 24, "bold"))

shape = Shape(last_shape)
grid[shape.y][shape.x]= shape.color


wn.listen()
wn.onkeypress(lambda: shape.move_left(grid), "Left")
wn.onkeypress(lambda: shape.move_right(grid), "Right")
#wn.onkeypress(lambda: shape.move_down(grid), "Down")
wn.onkeypress(lambda: shape.set_piece(grid), "space")
wn.onkeypress(lambda: shape.rotate_left(grid), "d")
wn.onkeypress(lambda: shape.rotate_right(grid), "a")
wn.onkeypress(lambda: shape.rotate_180(grid), "s")

score = 0

old_time = time.time()
running = True
while running:
    wn.update()

    if (time.time() - old_time) > .5:
        if shape.y == 19 - shape.height + 1:
            shape = Shape(last_shape)
            check_grid(grid)
        elif shape.can_move(grid):
            shape.erase_shape(grid)
            grid[shape.y][shape.x]= 0
            shape.y +=1
            shape.draw_shape(grid)
        else:
            if shape.y <= 4:
                running = False
                
            shape = Shape(last_shape)
            check_grid(grid)
            
        old_time = time.time() 

    draw_grid(pen, grid)
    draw_score(pen, score)
else:
    pen.clear()
    pen.hideturtle()
    pen.color("grey")
    pen.goto(-189, -3)
    pen.write("Game Over", move=False, align="left", font= ("Arial", 50, "bold"))
    pen.color("white")
    pen.goto(-187, 0)
    pen.write("Game Over", move=False, align="left", font= ("Arial", 50, "bold")) 
    
wn.mainloop()