import turtle as t
def rectangle(hotizontal,vertical,color):
	t.pendown()
	t.pensize(1)
	t.color(color)
	t.begin_fill()
	for conuter in range(1,3):
		t.forward(hotizontal)
		t.right(90)
		t.forward(vertical)
		t.right(90)
	t.end_fill()
	t.penup()
t.penup()
t.speed('fast')
t.bgcolor('black')

#feet
t.goto(-100,-150)
rectangle(50,20,'light blue')
t.goto(-30,-150)
rectangle(50,20,'light blue')

#legs
t.goto(-25,-50)
rectangle(15,100,'Seashell')
t.goto(-50,-50)
rectangle(-15,100,'Seashell')

#body
t.goto(-90,100)
rectangle(100,150,'blue')

#arms
t.goto(-150,70)
rectangle(60,15,'Seashell')
t.goto(-150,110)
rectangle(15,40,'Seashell')

t.goto(10,70)
rectangle(60,15,'Seashell')
t.goto(55,110)
rectangle(15,40,'Seashell')

#neck
t.goto(-50,120)
rectangle(15,20,'Seashell')

#head
t.goto(-85,170)
rectangle(80,50,'Seashell')

#eys
t.goto(-60,160)
rectangle(30,10,'white')
t.goto(-55,155)
rectangle(5,5,'black')
t.goto(-40,155)
rectangle(5,5,'black')

#mouth
t.goto(-65,135)
rectangle(40,5,'black')

t.hideturtle()


