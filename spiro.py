import turtle

hayley_turtle = turtle.Turtle()
hayley_turtle.color("blue")
hayley_turtle.pensize(4)
hayley_turtle.shape("turtle")
hayley_turtle.speed(7)
wn = turtle.Screen()

def draw_triangle(a_turtle, side_length):
	for each in range(0,3):
		a_turtle.forward(side_length)
		a_turtle.right(120)

def draw_spiro(a_turtle, side_length, num_of_tri):
	angle = 360 / num_of_tri
	for triangle in range(0, num_of_tri):
		draw_triangle(a_turtle, side_length)
		a_turtle.right(angle)

draw_spiro(hayley_turtle, 200, 15)
wn.exitonclick()