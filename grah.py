import turtle
turtle.shape('turtle')
length=2
for i in range(90):
    turtle.left(-5)
    for j in range(4):
        turtle.backward(5*i)
        turtle.left(90)
# Get drawing!
