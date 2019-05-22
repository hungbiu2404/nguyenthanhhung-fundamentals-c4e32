from turtle import *
def draw_star(x,y,length):
    penup()
    setposition(x,y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)
draw_star(50,0,100)
mainloop()
