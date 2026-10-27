import pygame

from src.settings import Settings
from src.ship import Ship


def test_ship_move_direita() -> None:
    """Testa se a nave se move para a direita quando moving_right é True."""
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    settings = Settings()

    ship = Ship(screen, settings)

    x_inicial = ship.x

    # ação
    ship.moving_right = True
    ship.update()

    # verificação
    assert ship.x > x_inicial


def test_ship_move_esquerda() -> None:
    """Testa se a nave se move para a esquerda quando moving_left é True."""
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    settings = Settings()

    ship = Ship(screen, settings)

    x_inicial = ship.x

    # ação
    ship.moving_left = True
    ship.update()

    # verificação
    assert ship.x < x_inicial


def test_ship_respects_screen_borders() -> None:
    """Testa se a nave respeita as bordas esquerda e direita da tela."""
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    settings = Settings()
    ship = Ship(screen, settings)

    # posiciona no limite esquerdo
    ship.rect.left = 0
    ship.x = float(ship.rect.x)
    ship.moving_left = True
    ship.update()
    assert ship.x == 0.0
