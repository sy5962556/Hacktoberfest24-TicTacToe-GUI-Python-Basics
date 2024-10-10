import turtle

def draw_heart(turtle):
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward (180)
    turtle.circle(-90, 200)
    turtle.setheading(60)
    turtle.circle(-90, 200)
    turtle.forward(180)
    turtle.end_fill()

def main():
    window = turtle.Screen()
    window.bgcolor('black')
    my_turtle = turtle.Turtle()
    my_turtle.speed(1)
    draw_heart(my_turtle)
    my_turtle.hideturtle()
    window.mainloop()

if __name__ == "__main__":
    main()
