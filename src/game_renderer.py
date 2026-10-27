import pygame
from pygame.surface import Surface

from alien import Alien
from bullet import Bullet
from interfaces import IRenderer
from ship import Ship


class GameRenderer(IRenderer):
    """Responsável apenas por desenhar os elementos do jogo na tela."""

    def __init__(
        self,
        screen: Surface,
        bg_color: tuple[int, int, int],
        ship: Ship,
        bullets: pygame.sprite.Group[Bullet],
        aliens: pygame.sprite.Group[Alien],
    ) -> None:
        self.screen: Surface = screen
        self.bg_color: tuple[int, int, int] = bg_color
        self.ship: Ship = ship
        self.bullets: pygame.sprite.Group[Bullet] = bullets
        self.aliens: pygame.sprite.Group[Alien] = aliens

    def _render_screen(self) -> None:
        """Redesenha a tela a cada passagem pelo laço."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self._draw_bullets()
        pygame.display.flip()

    def _draw_bullets(self) -> None:
        """Desenha os projéteis na tela."""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
