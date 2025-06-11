from historia import tela_inicial
import pygame
def main():
    pygame.mixer.init()
    pygame.mixer.music.load("medieval-background.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.03)
    tela_inicial()

if __name__ == "__main__":
    main()
