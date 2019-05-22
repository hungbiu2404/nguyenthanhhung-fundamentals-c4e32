from turtle import*
def square_draw(canh,colors):
    color(colors)
    for i in range(4):
        forward(canh)
        right(90)
    mainloop()
square_draw(100,'green')
