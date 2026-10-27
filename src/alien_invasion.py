import pygame
from pygame.surface import Surface

from bullet_manager import BulletManager
from fast_alien import FastAlien
from fleet_manager import FleetManager
from game_events import GameEventHandler
from game_renderer import GameRenderer
from interfaces import IBulletManager, IEventHandler, IFleetManager, IRenderer
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Gerencia o jogo e seus comportamentos dependendo de abstrações (DIP)."""

    def __init__(
        self,
        bullet_manager: IBulletManager | None = None,
        fleet_manager: IFleetManager | None = None,
        event_handler: IEventHandler | None = None,
        renderer: IRenderer | None = None,
    ) -> None:
        """Construtor da classe que inicializa o jogo e injeta abstrações."""
        pygame.init()
        self.settings: Settings = Settings()

        self.screen: Surface = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Criando uma instância da classe Ship para representar a nave espacial
        self.ship: Ship = Ship(self.screen, self.settings)

        # Mudando a cor do plano de fundo em RGB
        self.bg_color: tuple[int, int, int] = self.settings.bg_color

        # Injeção de dependências baseada em abstrações (DIP)
        self.bullet_manager: IBulletManager = bullet_manager or BulletManager(
            self.screen, self.settings, self.ship
        )
        self.fleet_manager: IFleetManager = fleet_manager or FleetManager(
            self.screen, self.settings, self.ship, FastAlien
        )
        self.event_handler: IEventHandler = event_handler or GameEventHandler(
            self.ship, self.bullet_manager
        )
        self.renderer: IRenderer = renderer or GameRenderer(
            self.screen,
            self.bg_color,
            self.ship,
            self.bullet_manager.bullets,
            self.fleet_manager.aliens,
        )

    def _update_game_state(self) -> None:
        """Atualiza a posição da nave, dos projéteis e dos alienígenas."""
        self.ship.update()
        self.bullet_manager._update_bullets(self.fleet_manager.aliens)
        self.fleet_manager._update_aliens()

    def run_game(self) -> None:
        """Cria um laço de repetição para a tela sempre ficar visível até
        que o usuário decida fechar a janela."""
        self.fleet_manager.create_fleet()

        while True:
            self.event_handler._check_events()
            self._update_game_state()
            self.renderer._render_screen()


if __name__ == "__main__":  # pragma: no cover
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
