import turtle

def draw_something(side_len, angle, num_sides):
    t = turtle.Turtle()
    t.setposition(0, 0)

    for i in range(num_sides):
        t.forward(side_len)
        t.right(angle)

