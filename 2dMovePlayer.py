# Changing the class so that the player is animated
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
BG = (121, 10, 120)

def draw_bg():
	screen.fill(BG)

class Soldier(pygame.sprite.Sprite):
	def __init__(self, char_type, x, y, scale, speed):
		pygame.sprite.Sprite.__init__(self)
		self.alive = True
		self.char_type = char_type
		self.speed = speed
		# direction and flip are variables that flip the image if the character is walking left.
		self.direction = 1
		self.flip = False
		self.animation_list = []
		self.frame_index = 0
		self.action = 0
		self.update_time = pygame.time.get_ticks()
		temp_list = []
		for i in range(2):
		# loading the image
			img = pygame.image.load(f'img/{self.char_type}/walk/alien{i}.png')
			img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
			temp_list.append(img)
		self.animation_list.append(temp_list)
		temp_list = []
		for i in range(2):
		# loading the image
			img = pygame.image.load(f'img/{self.char_type}/idle/alien{i}.png')
			img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
			temp_list.append(img)
		self.animation_list.append(temp_list)

		self.image = self.animation_list[self.action][self.frame_index]
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

	def move(self, moving_left, moving_right):
		# reset movement variables
		dx = 0
		dy = 0

		# assign movement variables if moving left or right
		if moving_left:
			# makes the speed a negative number
			dx = -self.speed
			# sets the flip value to true and the direction to -1
			self.flip = True
			self.direction = -1
			self.update_animation()
		if moving_right:
			# keeps the speed a positive number
			dx = self.speed
			# sets the flip value to False and the direction to 1
			self.flip = False
			self.direction = 1
			#self.update_animation()

		# update rectangle position.
		self.rect.x += dx
		self.rect.y += dy


	def update_animation(self):
		# update animation
		ANIMATION_COOLDOWN = 300
		# update image depending on current frame
		self.image = self.animation_list[self.action][self.frame_index]
		# check if enough time is passed since the last update
		if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
			self.update_time = pygame.time.get_ticks()
			self.frame_index += 1
		# if the animation has run out reset to the start
		if self.frame_index >= len(self.animation_list[self.action]):
			self.frame_index = 0

	def update_action(self, new_action):
		# check if the new action is different than the previous one.
		if new_action != self.action:
			self.action = new_action
			# update the animation settings.
			self.frame_index = 0
			self.update_time = pygame.time.get_ticks()

	def draw(self):
		# draws the image on the screen
		# if flip is true (the x value here) it flips the image on the x-axis.
		# if flip is false it doesn't flip it.
		# the y-axis flip is set permanently to false.
		screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


player = Soldier('player',200, 200, 0.5, 1)
enemy = Soldier('enemy', 400, 400, 0.5,1)


run = True

while run:
	clock.tick(FPS)

	draw_bg()

	player.update_animation()
	player.draw()

	# this if statement decides which animations to use depending on the 2D list index.
	if moving_right or moving_left:
		player.update_action(0) # 0 means walk
	else:
		player.update_action(1) # 1 means idle

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
