from pathlib import Path

import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface

from settings import Settings


class Alien(Sprite):
    """Gerencia os alienígenas (classe base para substituição de Liskov - LSP)."""

    def __init__(
        self, alien_invasion_screen: Surface, alien_invasion_settings: Settings
    ) -> None:
        """Inicializa o alienígena e define sua posição inicial."""
        super().__init__()
        self.screen: Surface = alien_invasion_screen
        self.settings: Settings = alien_invasion_settings

        # Localiza o caminho da imagem de forma segura independente de onde o script for iniciado
        base_dir = Path(__file__).resolve().parent.parent
        image_path = base_dir / "images" / "alien.bmp"
        if not image_path.exists():
            image_path = Path("images/alien.bmp")

        # Carrega a imagem do alienígena e obtém seu rect
        self.image: Surface = pygame.image.load(str(image_path))
        self.rect: pygame.Rect = self.image.get_rect()

        # Inicia cada novo alienígena próximo à parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x: float = float(self.rect.x)

    def drawme(self) -> None:
        """Desenha o alienígena em sua posição atual."""
        self.screen.blit(self.image, self.rect)

    def update(self) -> None:
        """Move o alienígena para a direita ou esquerda com base na direção da frota."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = int(self.x)

    def check_edges(self) -> bool:
        """Retorna True se o alienígena estiver na borda da tela."""
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0
