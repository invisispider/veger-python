# Veger
import turtle
import os
import math
import random
# import winsound

#Set up screen
wn = turtle.Screen()
wn.bgcolor("#050915")
wn.title("Bartleby Fights the Vegers")
wn.bgpic("bartlebg.gif")

#Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("invader2.gif")
turtle.register_shape("invader3.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("#ddccdd")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("orangered")
score_pen.penup()
score_pen.setposition(20, 310)
scorestring = "Points: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("GreenYellow")
player.shape("turtle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Choose a numer of enemies
number_of_enemies = 5
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
	#Create the enemy
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.shape("invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x, y)

enemyspeed = 8

#Draw title
title_pen = turtle.Turtle()
title_pen.speed(0)
title_pen.color("Red")
title_pen.penup()
title_pen.setposition(-280, 310)
titlestring = "Fight off the Vegers, Bartleby!"
title_pen.write(titlestring, False, align="left", font=("Arial", 14, "normal"))
title_pen.hideturtle()

#Create Turtle weapon
bullet = turtle.Turtle()
bullet.color("white")
bullet.shape("arrow")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.3, 0.3)
bullet.hideturtle()

bulletspeed = 50

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#Move left and right
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = -280
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)

def fire_bullet():
	#Declare bulletstate as a global if it needs changed
	global bulletstate
	if bulletstate == "ready":
		# winsound.PlaySound("boop", winsound.SND_ASYNC)
		bulletstate = "fire"
		#Move bullet to player
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x, y)
		bullet.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2)) 
	if distance < 30:
		return True
	else:
		return False

#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

isAlive = True

#Main game loop
while isAlive == True:

	if score >= 60:
		enemy.shape("invader2.gif")
	#	enemyspeed = 9
	elif score >= 140:
		enemy.shape("invader3.gif")
	#	enemyspeed = 12

	for enemy in enemies:
		#Enemy Initial Move
		n = enemy.xcor()
		n += enemyspeed
		enemy.setx(n)

		#Enemy Bounce and Pursuit
		if enemy.xcor() > 280 or enemy.xcor() < -280:
			#Move all enemies down
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1

		#Bullet enemy hit detect
		if isCollision(bullet, enemy):
			# winsound.PlaySound("drop.wav", winsound.SND_ASYNC)
            
			#Reset the bullet
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)
			#Reset the enemy
			x = random.randint(-200, 200)
			y = 250
			enemy.setposition(x, y)
			#Create Extra enemy
			enemy.penup()
			enemy.speed(0)
			x = random.randint(-200, 200)
			y = random.randint(100, 250)
			enemy.setposition(x, y)
			#Update score
			score += 10
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			title_pen.clear()
			titlestring = "They got you, pal! You lose!"
			title_pen.write(titlestring, False, align="left", font=("Arial", 14, "normal"))
			print ("Vegers Destroyed Bartlebuckets!")
			#break
			isAlive = False

		if enemy.ycor() <= -275:
			player.hideturtle()
			enemy.hideturtle()
			title_pen.clear()
			titlestring = "They got you, pal! You lose!"
			title_pen.write(titlestring, False, align="left", font=("Arial", 14, "normal"))
			print ("Vegers Got Conquest!")
			#break
			isAlive = False

		if score > 200:
			player.hideturtle()
			enemy.hideturtle()
			title_pen.clear()
			titlestring = "You did it, Bartleby! YOU WIN!!!"
			title_pen.write(titlestring, False, align="left", font=("Arial", 14, "normal"))
			print ("Bartleby Saved the day!")
			#break
			isAlive = False

	#Bullet motion
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)

	#Bullet boundary out
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"

wn.mainloop()
