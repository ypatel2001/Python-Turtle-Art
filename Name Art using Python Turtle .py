import turtle
t = turtle.Pen()
turtle.bgcolor("black")
Colors6 = ["red", "yellow", "blue", "orange", "green", "purple"]
colorchoice=int(turtle.textinput("Color Input",'''
You can use up to 6 colors for your picture.
1 = red
2 = red, yellow
3 = red, yellow, blue
4 = red, yellow, blue, orange
5 = red, yellow, blue, orange, green
6 = red, yellow, blue, orange, green, purple

Please enter your selection: '''))

circles= int(turtle.numinput("Number of circles","How many circles in your rosette?", 6))
if colorchoice==1:
        for x in range(circles):
            t.begin_fill()
            t.color(Colors6[x%colorchoice])
            t.pencolor(Colors6[x%colorchoice])
            t.circle(100)
            t.left(360/circles)
            t.end_fill()


if colorchoice==2:
        for x in range(circles):
           t.begin_fill()
           t.color(Colors6[x%colorchoice])
           t.pencolor(Colors6[x%colorchoice])
           t.circle(100)
           t.left(360/circles)
           t.end_fill()


if colorchoice==3:
       for x in range(circles):
            t.begin_fill()
            t.color(Colors6[x%colorchoice])
            t.pencolor(Colors6[x%colorchoice])
            t.circle(100)
            t.left(360/circles)
            t.end_fill()

if colorchoice==4:
        for x in range(circles):
            t.begin_fill()
            t.color(Colors6[x%colorchoice])
            t.pencolor(Colors6[x%colorchoice])
            t.circle(100)
            t.left(360/circles)
            t.end_fill()
        

if colorchoice==5:
        for x in range(circles):
            begin_fill
            t.color(Colors6[x%colorchoice])
            t.pencolor(Colors6[x%colorchoice])
            t.circle(100)
            t.left(360/circles)
            end_fill


if colorchoice==6:
        for x in range(circles):
            t.begin_fill()
            t.color(Colors6[x%colorchoice])
            t.pencolor(Colors6[x%colorchoice])
            t.circle(100)
            t.left(360/circles)
            t.end_fill()




