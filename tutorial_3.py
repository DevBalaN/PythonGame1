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
move_esquerda = False
move_direita = False

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

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, velocidade, tamanho):
		pygame.sprite.Sprite.__init__(self)
		self.vel = velocidade
		self.giro = False
		self.lista = []
		self.frame = 0
		self.update_time = pygame.time.get_ticks()
		for i in range(8):
			img = pygame.image.load(f'imagens/heroi/parado/{i}.png').convert_alpha()
			img = pygame.transform.scale(img, (int(img.get_width() * tamanho), int(img.get_height() * tamanho)))
			self.lista.append(img)
		self.imagem = self.lista[self.frame]
		self.rect = self.imagem.get_rect()
		self.rect.center = (x, y)

	def update(self):
		heroi.animation()

	def move(self, move_esquerda, move_direita):
		dx = 0
		dy = 0

		if move_esquerda:
			dx = -self.vel
			self.giro = True
		if move_direita:
			dx = self.vel
			self.giro = False

		self.rect.x += dx

	def animation(self):
		animation_cooldown = 100
		self.imagem = self.lista[self.frame]
		if pygame.time.get_ticks() - self.update_time > animation_cooldown:
			self.update_time = pygame.time.get_ticks()
			self.frame += 1
		if self.frame >= 8:
			self.frame = 0


	def draw(self):
		tela.blit(pygame.transform.flip(self.imagem, self.giro, False), self.rect)

heroi = Player(100, 450, 1 , 1)


iniciar = True
while iniciar:
	relogio.tick(fps)

	fundo()
	grade()

	heroi.move(move_esquerda, move_direita)	
	heroi.update()
	heroi.draw()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			iniciar = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				move_esquerda = True
			if event.key == pygame.K_RIGHT:
				move_direita = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				move_esquerda = False
			if event.key == pygame.K_RIGHT:
				move_direita = False

	pygame.display.update() # atualiza a tela

pygame.quit()