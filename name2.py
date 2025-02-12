import turtle

def write_name():
    turtle.color('blue')
    style = ('Courier', 90, 'normal')
    turtle.write('OMAR', font=style, align='center')
    turtle.hideturtle()
    turtle.exitonclick()
write_name()