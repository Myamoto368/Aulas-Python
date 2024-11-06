import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Carregar música de fundo
pygame.mixer.music.load(r"C:\Users\Senai\Desktop\Vitor Lopes\Cadastro\yt5s.com - Original Tetris theme (Tetris Soundtrack) (128 kbps).mp3")
pygame.mixer.music.play(-1)  # Toca a música em loop

# Carregar imagem de fundo
background_image = pygame.image.load(r"C:\Users\Senai\Desktop\Vitor Lopes\Cadastro\1920x1080.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))  # Redimensiona a imagem para caber na tela

# Classe para a Nave do Jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 15  # Aumenta a velocidade de movimento
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += 15  # Aumenta a velocidade de movimento

    def shoot(self):
        if len(bullets) < 5:  # Limita o número de balas na tela
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)

# Classe para os Disparos
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y -= 15  # Aumenta a velocidade da bala
        if self.rect.bottom < 0:
            self.kill()

# Classe para os Alienígenas
class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((30, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction = random.choice([-1, 1])  # Direção inicial aleatória

    def update(self):
        # Movimento lateral
        self.rect.x += self.direction * 3  # Reduz a velocidade lateral

        # Verifica as bordas da tela
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.direction *= -1  # Inverte a direção
            self.rect.y += 10  # Desce mais quando atinge a borda

        # Movimento vertical constante
        self.rect.y += self.speed

        if self.rect.top > screen_height:
            self.kill()

# Grupos de sprites
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
aliens = pygame.sprite.Group()

# Inicializa o jogador
player = Player()
all_sprites.add(player)

def create_aliens(rows, cols, speed):
    """Cria alienígenas em uma formação ordenada."""
    for row in range(rows):
        for col in range(cols):
            alien = Alien(50 + col * 100, 50 + row * 40, speed)
            all_sprites.add(alien)
            aliens.add(alien)

# Parâmetros iniciais
initial_rows = 3
initial_cols = 5
initial_speed = 0.5  # A velocidade inicial de queda dos alienígenas

# Cria alienígenas para a fase inicial
create_aliens(initial_rows, initial_cols, initial_speed)

# Função para exibir a pontuação
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x, y))
    surf.blit(text_surface, text_rect)

# Loop do jogo
running = True
score = 0
level = 1
rows = initial_rows
cols = initial_cols
speed = initial_speed

# Variáveis de disparo
shooting = False
last_shot_time = 0
shot_interval = 0.25  # Intervalo de 0.25 segundos para 4 tiros por segundo

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shooting = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shooting = False

    # Atualiza
    all_sprites.update()

    # Verifica se o jogador está atirando
    if shooting:
        current_time = pygame.time.get_ticks()
        if current_time - last_shot_time >= shot_interval * 1000:  # Converte para milissegundos
            player.shoot()
            last_shot_time = current_time

    # Verifica colisões entre disparos e alienígenas
    hits = pygame.sprite.groupcollide(bullets, aliens, True, True)
    for hit in hits:
        score += 10

    # Verifica se todos os alienígenas foram eliminados
    if not aliens:
        pygame.time.wait(500)  # Aguarda meio segundo antes de aumentar o nível
        level += 1
        rows = int(rows * 1.2)
        cols = int(cols * 1.2)
        speed += 0.025  # Aumenta a velocidade em cada nível
        create_aliens(rows, cols, speed)
        bullets.empty()
    elif level > 1 and not aliens:  # Se não houver alienígenas e já passou o primeiro nível
        print("Você ganhou o nível!")  # Adiciona mensagem de vitória no nível
    elif level > 1 and aliens:  # Verifica se há alienígenas restantes
        print("Game Over! Você perdeu!")  # Adiciona mensagem de Game Over
        running = False  # Encerra o jogo

    # Desenha
    screen.blit(background_image, (0, 0))  # Desenha a imagem de fundo
    all_sprites.draw(screen)
    draw_text(screen, f'Score: {score}', 36, screen_width // 2, 20)
    draw_text(screen, f'Level: {level}', 36, screen_width // 2, 50)
    pygame.display.flip()

    # FPS
    pygame.time.Clock().tick(60)

# Tela de Game Over
screen.fill(BLACK)
draw_text(screen, 'GAME OVER', 64, screen_width // 2, screen_height // 2 - 20)
draw_text(screen, f'Final Score: {score}', 36, screen_width // 2, screen_height // 2 + 20)
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
