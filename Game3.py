import pygame
import math

point = 0
x = 0
y = 0
l = 0
r = 1
acceleration = 0
gravity = 0.5
distance1 = 0
distance2 = 0

pygame.init()

WIDTH, HEIGHT = 1000, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Images
dirt = pygame.image.load("Dirt.png")
sky = pygame.image.load("Sky.png")
cloud = pygame.image.load("Cloud.png")
sun = pygame.image.load("Sun.png")
board = pygame.image.load("Board.png")
enemy = pygame.image.load("ENEMY.png")
wall = pygame.image.load("WALL.png")


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	#Sky
	for y1 in range(0,HEIGHT-100,100):
		for x1 in range(0,WIDTH,100):
			screen.blit(sky, (x1, y1))
	
	#Boundary
	if x >= 1000:
		x = 1000
		l = 0
		r = 1
		point += 1

	if x <= -1000:
		x = -1000
		l = 1
		r = 0
		point += 1

	#Left
	if l == 1:
		x+=5 + (point * 0.2)

	#Right
	if r == 1:
		x-=5 + (point * 0.2)

	keys = pygame.key.get_pressed()	

	#Jump
	if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and y == 0: 
		acceleration = 20

	if acceleration > 0:
		acceleration -= 0.5
		y -= gravity * acceleration
			
	if acceleration <= 0 and y < 0:
		acceleration -= 0.5 
		y -= gravity * acceleration

		if y >= -5:
			y = 0
			acceleration = 0

	#Images
	screen.blit(cloud,(700,50))
	screen.blit(cloud,(600,200))
	screen.blit(cloud,(300,100))
	screen.blit(cloud,(100,200))
	screen.blit(sun,(50,50))
	screen.blit(board,(450,510+y))
	
	#Enemy 1
	screen.blit(enemy,(x+300,540))
	
	p1 = (x+300,540)
	p2 = (450,510+y)
	distance1 = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

	if distance1 < 70:
		point = 0

	#Enemy2
	if point >= 5:
		screen.blit(enemy,(x+350,540))
		
		p3 = (x+350,540)
		p2 = (450,510+y)
	
		#Using pythagorean theorem
		distance2 = math.sqrt(((p3[0]-p2[0])**2)+((p3[1]-p2[1])**2))

		if distance2 < 70:
			point = 0

	#Score
	text1 = pygame.font.SysFont('Verdana', 50)
	line1 = f"Score: {point}"
	text1 = pygame.font.Font.render(text1,line1,True, (255,255,0))
	rect = text1.get_rect()
	rect.center = (860,50)
	screen.blit(text1,rect)

	#Ground
	for x1 in range(-1000,WIDTH+1000,100):
		screen.blit(dirt, (x1+x, 600))

	#Boundary
	screen.blit(wall,(x+1540,520))
	screen.blit(wall,(x+1540,420))
	screen.blit(wall,(x-635,420))
	screen.blit(wall,(x-635,520))
		
	pygame.display.update()
	pygame.event.pump()

	





