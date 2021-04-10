import pygame

pygame.init() # inicializar a biblioteca

tela_x = 800
tela_y = 600

tela = pygame.display.set_mode((tela_x, tela_y))
pygame.display.set_caption('Teste')

img_fundo = pygame.image.load('ceu.png').convert_alpha()

#função para desenha a imagem de fundo
def fundo():
	tela.blit(img_fundo, (0, 0))

iniciar = True
while iniciar:

	fundo()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			iniciar = False

	pygame.display.update() # atualiza a tela

pygame.quit()
