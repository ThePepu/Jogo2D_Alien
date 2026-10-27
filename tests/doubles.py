import pygame

from src.alien import Alien
from src.bullet import Bullet
from src.interfaces import IBulletManager, IFleetManager


class StubBulletManager(IBulletManager):
    """Stub que simula o gerenciador de projéteis com respostas controladas."""

    def __init__(self) -> None:
        self.bullets: pygame.sprite.Group[Bullet] = pygame.sprite.Group()
        self.fired_count: int = 0
        self.updated_count: int = 0

    def _fire_bullet(self) -> None:
        self.fired_count += 1

    def _update_bullets(self, aliens: pygame.sprite.Group[Alien]) -> None:
        self.updated_count += 1


class StubFleetManager(IFleetManager):
    """Stub que simula o gerenciador de frota com respostas controladas."""

    def __init__(self) -> None:
        self.aliens: pygame.sprite.Group[Alien] = pygame.sprite.Group()
        self.fleet_created: bool = False
        self.updated_count: int = 0

    def create_fleet(self) -> None:
        self.fleet_created = True

    def _update_aliens(self) -> None:
        self.updated_count += 1
