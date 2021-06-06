# fixing the trail and moving the player
import pygame

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('shooter')

#set frame rate
clock = pygame.time.Clock()
FPS = 60

# define player action variables
moving_left = False
moving_right = False

# define colours
BG = (144, 10, 120)

def draw_bg():
	screen.fill(BG)

class Soldier(pygame.sprite.Sprite):
	def __init__(self, x, y, scale, speed):
		pygame.sprite.Sprite.__init__(self)
		self.speed = speed
		img = pygame.image.load('img/player/walk/alien0.png')
		self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

	def move(self, moving_left, moving_right):
		# reset movement variables
		dx = 0
		dy = 0

		# assign movement variables if moving left or right
		if moving_left:
			dx = -self.speed
		if moving_right:
			dx = self.speed

		# update rectangle position.
		self.rect.x += dx
		self.rect.y += dy

	def draw(self):
		screen.blit(self.image, self.rect)


player = Soldier(200, 200, 0.5, 1)


run = True

while run:
	clock.tick(FPS)

	draw_bg()

	player.draw()
	player.move(moving_left, moving_right)

	for event in pygame.event.get():
		# quit game
		if event.type == pygame.QUIT:
			run = False

		# keyboard presses
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				moving_left = True
			if event.key == pygame.K_d:
				moving_right = True
			if event.key == pygame.K_ESCAPE:
				run = False

		# keyboard releases
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				moving_left = False
			if event.key == pygame.K_d:
				moving_right = False


	pygame.display.update()

pygame.QUIT()
