from turtle import *
canvas = Screen()
canvas.setup(512,512)
bgcolor("#111823")


title("Valorant Logo")
ht()

def logo(color="#ff4655"):
	fillcolor(color)
	pencolor(color)

	begin_fill()
	up()
	goto(-135,111)
	rt(90)
	down()
	fd(111)
	setheading(-51)
	fd(141)
	setheading(0)
	fd(88)
	goto(-135,111)
	end_fill()

	up()
	home()
	fd(17)
	rt(90)
	fd(35)
	down()
	begin_fill()
	setheading(0)
	fd(88)
	setheading(51.1)
	fd(46.23)
	setheading(0)
	lt(90)
	fd(110)
	setheading(-128.7)
	fd(187)
	end_fill()
	up()
	home()
	down()

while True:
	for i in ["#ff4655", "#ffa500", "#ffff00", "#008000", "#0000ff", "#4b0082", "#ee82ee", "#ff4655"]:
		logo(i)
