import pygame

pygame.init() # inicializar a biblioteca

relogio = pygame.time.Clock()
fps = 60

tela_x = 800
tela_y = 600


tela = pygame.display.set_mode((tela_x, tela_y))
pygame.display.set_caption('Teste')

#variaveis de cores
vermelho = (255, 0, 0)
verde = (0, 255, 100)
azul = (0, 0, 255)
branco = (255, 255, 255)
perto = (0, 0, 0)

#variaveis do personagem
dx = 0
dy = 0

img_ceu = pygame.image.load('imagens/ceu.png').convert_alpha()
img_montanha = pygame.image.load('imagens/montanha.png').convert_alpha()
img_barranco = pygame.image.load('imagens/barranco.png').convert_alpha()

#função para desenha a imagem de fundo
def fundo():
	tela.fill(verde)
	tela.blit(img_ceu, (0, 0))
	tela.blit(img_montanha, (0, 50))
	tela.blit(img_barranco, (0, 350))

def grade():
	for l in range(16):
		pygame.draw.line(tela, branco, (0, l * 50), (800 , l * 50))
	for c in range(16):
		pygame.draw.line(tela, branco, (c * 50, 0), (c * 50, 600))


iniciar = True
while iniciar:
	relogio.tick(fps)

	fundo()
	grade()

	pygame.draw.rect(tela, vermelho, [dx, dy, 50, 100])

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			iniciar = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				dy -= 50
			if event.key == pygame.K_LEFT:
				dx -= 50
			if event.key == pygame.K_DOWN:
				dy += 50
			if event.key == pygame.K_RIGHT:
				dx += 50


	pygame.display.update() # atualiza a tela

pygame.quit()
