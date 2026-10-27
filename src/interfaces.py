from abc import ABC, abstractmethod

import pygame

from alien import Alien
from bullet import Bullet


class IUpdatable(ABC):
    """Interface segregada apenas para entidades que atualizam estado (ISP)."""

    @abstractmethod
    def update(self) -> None:
        """Atualiza o estado da entidade."""


class IBulletManager(ABC):
    """Abstração para gerenciamento de projéteis (ISP & DIP)."""

    bullets: pygame.sprite.Group[Bullet]

    @abstractmethod
    def _fire_bullet(self) -> None:
        """Dispara um novo projétil."""

    @abstractmethod
    def _update_bullets(self, aliens: pygame.sprite.Group[Alien]) -> None:
        """Atualiza projéteis ativos e verifica colisões."""


class IFleetManager(ABC):
    """Abstração para gerenciamento da frota de alienígenas (ISP & DIP)."""

    aliens: pygame.sprite.Group[Alien]

    @abstractmethod
    def create_fleet(self) -> None:
        """Cria a frota de alienígenas."""

    @abstractmethod
    def _update_aliens(self) -> None:
        """Atualiza o posicionamento da frota."""


class IEventHandler(ABC):
    """Abstração para tratamento de eventos de entrada (ISP & DIP)."""

    @abstractmethod
    def _check_events(self) -> None:
        """Processa eventos do teclado e janela."""


class IRenderer(ABC):
    """Abstração para renderização gráfica do jogo (ISP & DIP)."""

    @abstractmethod
    def _render_screen(self) -> None:
        """Renderiza os elementos visuais na tela."""
