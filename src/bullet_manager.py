import pygame
from pygame.surface import Surface

from alien import Alien
from bullet import Bullet
from interfaces import IBulletManager
from settings import Settings
from ship import Ship


class BulletManager(IBulletManager):
    """Responsável apenas por criar, atualizar e desenhar os projéteis."""

    def __init__(self, screen: Surface, settings: Settings, ship: Ship) -> None:
        self.screen: Surface = screen
        self.settings: Settings = settings
        self.ship: Ship = ship
        self.bullets: pygame.sprite.Group[Bullet] = pygame.sprite.Group()

    def _fire_bullet(self) -> None:
        """Dispara um projétil se o limite de projéteis ainda não tiver sido alcançado."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self.screen, self.settings, self.ship)
            self.bullets.add(new_bullet)

    def _update_bullets(self, aliens: pygame.sprite.Group[Alien]) -> None:
        """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""
        self.bullets.update()
        self._remove_offscreen_bullets()
        self._check_bullet_alien_collisions(aliens)

    def _remove_offscreen_bullets(self) -> None:
        """Remove os projéteis que desapareceram da tela."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(
        self, aliens: pygame.sprite.Group[Alien]
    ) -> None:
        """Verifica colisões entre projéteis e alienígenas."""
        pygame.sprite.groupcollide(self.bullets, aliens, True, True)
