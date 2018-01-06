import turtle

def draw():
    window = turtle.Screen()
    window.bgcolor("grey")

    brad = turtle.Turtle()
    brad.shape('arrow')
    brad.color('yellow')
    brad.speed(5)

    i = 0
    for i in range(1,160):
        if i % 2 == 0:
            brad.color('red')
        if i % 4 == 0 :
            brad.color('yellow')
        brad.forward(100)
        brad.right(90)
        
        
        if i % 4 == 0:
            brad.right(10)
        #cir = turtle.Turtle()
        #cir.color('blue')
        #cir.circle(100)
    brad.shape('')
    window.exitonclick()

draw()
