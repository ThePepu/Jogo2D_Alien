import sys

import pygame

try:
    from settings import Settings
    from ship import Ship
except ImportError:
    from src.settings import Settings
    from src.ship import Ship


class AlienInvasion:
    """Classe principal para gerenciamento do jogo e seus comportamentos."""

    def __init__(self):
        """Construtor da classe que inicializa o jogo e cria os recursos básicos do jogo."""
        pygame.init()
        self.settings = Settings()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Cria a instância da nave espacial
        self.ship = Ship(self.screen, self.settings)

    def run_game(self):
        """Criando um laço de repetição para a tela sempre ficar visível até que
        o usuário decida fechar a janela."""
        while True:
            # "ouvindo" algum evento no mouse ou teclado.
            # para acessa aos eventos que o Pygame me detecta, só chamar o método event.get()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # encerra o jogo.

            # Redesenha a tela com a cor de fundo definida nas configurações
            self.screen.fill(self.settings.bg_color)

            # Desenha a nave espacial na tela
            self.ship.blitme()

            # Tornando visível a tela desenhada recentemente
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    # Fazendo uma instancia da classe.
    alien_invasion = AlienInvasion()
    # Após instanciar um objeto, ele pode realizar a chamada de seus comportamentos.
    # Nesse momento, vamos chamar o run_game.
    alien_invasion.run_game()
