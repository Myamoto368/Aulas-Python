import pygame
import random

# Inicialização do pygame
pygame.init()

# Configurações de tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Forca')

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Fonte
fonte = pygame.font.Font(None, 36)
fonte_grande = pygame.font.Font(None, 48)

# Lista de palavras
palavras = [
    'python', 'programacao', 'jogo', 'desenvolvedor', 'pygame', 
    'computador', 'internet', 'inteligencia', 'artificial', 
    'algoritmo', 'variavel', 'função', 'classe', 'objeto', 
    'sistema', 'rede', 'servidor', 'dados', 'banco', 
    'análise', 'estudo', 'teoria', 'prática', 'experiência', 
    'tecnologia', 'software', 'hardware', 'programa', 
    'aplicativo', 'criptografia', 'segurança', 'sistemas', 
    'interface', 'usuario', 'experimento', 'modelo', 
    'simulação', 'otimização', 'desempenho', 'diagnóstico'
]

# Função para selecionar uma palavra aleatória
def escolher_palavra():
    return random.choice(palavras).upper()

# Função para desenhar a forca e o boneco
def desenhar_forca(tela, erros):
    pygame.draw.line(tela, PRETO, (50, 500), (200, 500), 5)  # Base
    pygame.draw.line(tela, PRETO, (125, 500), (125, 150), 5)  # Poste
    pygame.draw.line(tela, PRETO, (125, 150), (250, 150), 5)  # Braço superior
    pygame.draw.line(tela, PRETO, (250, 150), (250, 200), 5)  # Corda

    if erros > 0:
        pygame.draw.circle(tela, PRETO, (250, 230), 30, 5)  # Cabeça
    if erros > 1:
        pygame.draw.line(tela, PRETO, (250, 260), (250, 350), 5)  # Corpo
    if erros > 2:
        pygame.draw.line(tela, PRETO, (250, 280), (200, 320), 5)  # Braço esquerdo
    if erros > 3:
        pygame.draw.line(tela, PRETO, (250, 280), (300, 320), 5)  # Braço direito
    if erros > 4:
        pygame.draw.line(tela, PRETO, (250, 350), (200, 400), 5)  # Perna esquerda
    if erros > 5:
        pygame.draw.line(tela, PRETO, (250, 350), (300, 400), 5)  # Perna direita

# Função para desenhar as letras da palavra
def desenhar_palavra(tela, palavra, letras_adivinhadas):
    mostrar_palavra = ''
    for letra in palavra:
        if letra in letras_adivinhadas:
            mostrar_palavra += letra + ' '
        else:
            mostrar_palavra += '_ '
    texto = fonte.render(mostrar_palavra, True, PRETO)
    tela.blit(texto, (400, 350))

# Função para desenhar letras erradas
def desenhar_letras_erradas(tela, letras_erradas):
    texto = fonte.render('Letras erradas: ' + ' '.join(letras_erradas), True, VERMELHO)
    tela.blit(texto, (400, 450))

# Função para desenhar o contador de erros
def desenhar_contador_erros(tela, erros, max_erros):
    texto = fonte.render(f'Erros: {erros} / {max_erros}', True, VERMELHO)
    tela.blit(texto, (600, 50))

# Função para desenhar o botão de reiniciar
def desenhar_botao_reiniciar(tela):
    texto = fonte.render("Reiniciar", True, BRANCO)
    largura_texto = texto.get_width()
    altura_texto = texto.get_height()
    rect_botao = pygame.Rect((largura // 2 - largura_texto // 2 - 10, 500, largura_texto + 20, altura_texto + 20))
    pygame.draw.rect(tela, AZUL, rect_botao)
    tela.blit(texto, (largura // 2 - largura_texto // 2, 510))
    return rect_botao

# Função principal do jogo
def main():
    clock = pygame.time.Clock()
    palavra_secreta = escolher_palavra()
    letras_adivinhadas = []
    letras_erradas = []
    erros = 0
    max_erros = 6  # Definindo o máximo de erros permitido
    ganhou = False
    rodando = True
    jogo_finalizado = False
    rect_botao = None

    while rodando:
        tela.fill(BRANCO)  # Limpar a tela
        desenhar_forca(tela, erros)
        desenhar_palavra(tela, palavra_secreta, letras_adivinhadas)
        desenhar_letras_erradas(tela, letras_erradas)
        desenhar_contador_erros(tela, erros, max_erros)

        if jogo_finalizado:
            rect_botao = desenhar_botao_reiniciar(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.KEYDOWN and not jogo_finalizado:
                letra = event.unicode.upper()
                if letra.isalpha() and letra not in letras_adivinhadas and letra not in letras_erradas:
                    if letra in palavra_secreta:
                        letras_adivinhadas.append(letra)
                    else:
                        letras_erradas.append(letra)
                        erros += 1

            elif event.type == pygame.MOUSEBUTTONDOWN and jogo_finalizado:
                if rect_botao and rect_botao.collidepoint(event.pos):
                    # Reiniciar o jogo
                    palavra_secreta = escolher_palavra()
                    letras_adivinhadas = []
                    letras_erradas = []
                    erros = 0
                    ganhou = False
                    jogo_finalizado = False

        if not jogo_finalizado:
            if all(letra in letras_adivinhadas for letra in palavra_secreta):
                ganhou = True
                jogo_finalizado = True
            if erros >= max_erros:
                jogo_finalizado = True

        if jogo_finalizado:
            mensagem = "Você ganhou!" if ganhou else f"Você perdeu! A palavra era: {palavra_secreta}"
            cor_mensagem = PRETO if ganhou else VERMELHO
            texto = fonte_grande.render(mensagem, True, cor_mensagem)
            tela.blit(texto, (largura // 2 - texto.get_width() // 2, 50))  # Mensagem no topo da tela

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
 