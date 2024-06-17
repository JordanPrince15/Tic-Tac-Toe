import turtle

#Background
wn = turtle.Screen()
wn.screensize(600, 800)
wn.bgcolor('white')
wn.title('Tic Tac Toe')

#Turtle
Grid = turtle.Turtle()
Grid.speed('fastest')
Grid.pensize(2)
Grid.penup()
x = 300 
y = 300
Grid.goto(x, y)



def DrawGrid():
    for grid in range(0, 4): # This draws the initial SquareGrid
        Grid.pendown()
        Grid.right(90)
        Grid.forward(600)
        Grid.penup()


    Grid.pendown() #This draws the inner blocks
    Grid.goto(300, 100)
    Grid.goto(-300, 100)
    Grid.goto(-300, -100)
    Grid.goto(300, -100)

    Grid.goto(300, -300)
    Grid.goto(100, -300)
    Grid.goto(100, 300)
    Grid.goto(-100, 300)
    Grid.goto(-100, -300)

    Grid.pendown()

def CrossClick(qX, qY):
    if (qX >= -300 and qX < -100) and (qY >= -300 and qY < -100): # Quad 1
        # Grid.penup()
        Grid.goto(-300, -300)
        Grid.pendown()
        Grid.goto(-100, -100)
        Grid.goto(-100, -300)
        Grid.goto(-300, -300)
        Grid.goto(-300, -100)
        Grid.goto(-100, -300)

    if (qX >= -100 and qX < 100) and (qY >= -300 and qY < -100): # Quad 2
        Grid.penup()
        Grid.goto(-100, -300)
        Grid.pendown()
        Grid.goto(100, -100)
        Grid.goto(100, -300)
        Grid.goto(-100, -300)
        Grid.goto(-100, -100)
        Grid.goto(100, -300)

    if (qX >= 100 and qX < 300) and (qY >= -300 and qY < -100): # Quad 3
        Grid.penup()
        Grid.goto(100, -300)
        Grid.pendown()
        Grid.goto(300, -100)
        Grid.goto(300, -300)
        Grid.goto(100, -300)
        Grid.goto(100, -100)
        Grid.goto(300, -300)

    if (qX >= -300 and qX < -100) and (qY >= -100 and qY < 100): # Quad 4
    
        Grid.penup()
        Grid.goto(-100, -100)
        Grid.pendown()
        Grid.goto(-100, 100)
        Grid.goto(-300, -100)
        Grid.goto(-300, -100)
        Grid.goto(-300, 100)
        Grid.goto(-100, -100)

    if (qX >= -100 and qX < 100) and (qY >= -100 and qY < 100): # Quad 5
        Grid.penup()
        Grid.goto(-100, -100)
        Grid.pendown()
        Grid.goto(100, 100)
        Grid.goto(100, -100)
        Grid.goto(-100, -100)
        Grid.goto(-100, 100)
        Grid.goto(100, -100)

    if (qX >= 100 and qX < 300) and (qY >= -100 and qY < 100): # Quad 6
            
            Grid.penup()
            Grid.goto(100, -100)
            Grid.pendown()
            Grid.goto(300, 100)
            Grid.goto(300, -100)
            Grid.goto(100, -100)
            Grid.goto(100, 100)
            Grid.goto(300, -100)

    if (qX >= -300 and qX < -100) and (qY >= 100 and qY < 300): # Quad 7
    
        Grid.penup()
        Grid.goto(-100, 100)
        Grid.pendown()
        Grid.goto(-100, 300)
        Grid.goto(-300, 100)
        Grid.goto(-300, 100)
        Grid.goto(-300, 300)
        Grid.goto(-100, 100)

    if (qX >= -100 and qX < 100) and (qY >= 100 and qY < 300): # Quad 8
        Grid.penup()
        Grid.goto(-100, 100)
        Grid.pendown()
        Grid.goto(100, 300)
        Grid.goto(100, 100)
        Grid.goto(-100, 100)
        Grid.goto(-100, 300)
        Grid.goto(100, 100)

    if (qX >= 100 and qX < 300) and (qY >= 100 and qY < 300): # Quad 9
            
        Grid.penup()
        Grid.goto(100, 100)
        Grid.pendown()
        Grid.goto(300, 300)
        Grid.goto(300, 100)
        Grid.goto(100, 100)
        Grid.goto(100, 300)
        Grid.goto(300, 100)

def CircleClick(qX, qY):
    if (qX >= -300 and qX < -100) and (qY >= -300 and qY < -100): # Quad 1
        # Grid.penup()
        Grid.goto(-200, -280)
        Grid.pendown()
        Grid.circle(80)
        Grid.penup()

    if (qX >= -100 and qX < 100) and (qY >= -300 and qY < -100): # Quad 2
        Grid.penup()
        Grid.goto(0, -280)
        Grid.pendown()
        Grid.circle(80)
        Grid.penup()

    if (qX >= 100 and qX < 300) and (qY >= -300 and qY < -100): # Quad 3
        Grid.penup()
        Grid.goto(200, -280)
        Grid.pendown()
        Grid.circle(80)
        Grid.penup()

    if (qX >= -300 and qX < -100) and (qY >= -100 and qY < 100): # Quad 4
    
        Grid.penup()
        Grid.goto(-200, -80)
        Grid.pendown()
        Grid.circle(80)
        Grid.penup()

    if (qX >= -100 and qX < 100) and (qY >= -100 and qY < 100): # Quad 5
        Grid.penup()
        Grid.goto(0, -80)
        Grid.pendown()
        Grid.circle(80)
        Grid.penup()

    if (qX >= 100 and qX < 300) and (qY >= -100 and qY < 100): # Quad 6
            
            Grid.penup()
            Grid.goto(200, -80)
            Grid.pendown()
            Grid.circle(80)
            Grid.penup()

    if (qX >= -300 and qX < -100) and (qY >= 100 and qY < 300): # Quad 7
    
        Grid.penup()
        Grid.goto(-200, 120)
        Grid.pendown()
        Grid.circle(80)
        Grid.penup()

    if (qX >= -100 and qX < 100) and (qY >= 100 and qY < 300): # Quad 8
        Grid.penup()
        Grid.goto(0, 120)
        Grid.pendown()
        Grid.circle(80)
        Grid.penup()

    if (qX >= 100 and qX < 300) and (qY >= 100 and qY < 300): # Quad 9
            
        Grid.penup()
        Grid.goto(200, 120)
        Grid.pendown()
        Grid.circle(80)
        Grid.penup()
 

def main():
    DrawGrid()
    
if __name__ == '__main__':
    main()
wn.listen()
wn.onscreenclick(CrossClick, 1)
wn.onscreenclick(CircleClick, 3)

wn.mainloop()