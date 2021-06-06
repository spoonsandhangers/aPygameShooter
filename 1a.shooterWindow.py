import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('shooter')

# picture being loaded
x = 200
y = 200
scale = 0.5
img = pygame.image.load('img/player/idle/alien0.png')
# picture being scaled
img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
rect = img.get_rect()
rect.center = (x, y)


run = True

while run:

	screen.blit(img, rect)


	for event in pygame.event.get():
		# quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.QUIT()
