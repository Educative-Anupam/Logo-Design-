
import turtle as t
screen=t.Screen()
screen.bgcolor("white")

def draw_oval():
    t.penup()
    t.goto(145,0)
    t.pendown()
    t.color("red")
    t.begin_fill()

    t.left(45)
    for _ in range(2):
        t.circle(55,90)
        t.circle(275,90)

    t.end_fill()

def write_name():
     t.penup()
     t.goto(-40,0)
     t.pendown()
     t.color("white")
     t.write("Sashyashree", align="center",font=("Impact",50,"bold"))

def draw_circle():
     t.penup()
     t.goto(155,0)
     t.pendown()
     t.color("red")
     t.width(4)
     t.left(0)
     for _ in range(2):
         t.circle(58,90)
         t.circle(288,90)

def make_draw():
    t.penup()
    t.goto(165,0)
    t.pendown()
    t.color("red")
    t.width(4)
    t.left(0)
    for _ in range(2):
        t.circle(62,90)
        t.circle(305,90)

def Write():
    t.penup()
    t.goto(-55,-150)
    t.pendown()
    t.color("black")
    t.write("A TRUSTED BRAND",align="center",font=("Arial",20,"bold"))

draw_oval()
write_name()
draw_circle()
make_draw()
Write()

t.exitonclick()