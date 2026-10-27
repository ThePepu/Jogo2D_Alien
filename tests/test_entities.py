import pygame
import pytest
from pygame.surface import Surface

from src.alien import Alien
from src.bullet import Bullet
from src.fast_alien import FastAlien
from src.settings import Settings
from src.ship import Ship


@pytest.fixture
def game_env() -> tuple[Surface, Settings]:
    """Fixture para preparar a tela e as configurações antes dos testes."""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((800, 600))
    return screen, settings


def test_settings_default_values() -> None:
    """Testa valores padrões de configuração usando Assert simples."""
    settings = Settings()
    assert settings.screen_width == 1200, (
        f"Esperado 1200, mas obteve {settings.screen_width}"
    )
    assert settings.screen_height == 800
    assert settings.bullet_allowed == 1


def test_alien_movement_with_fixture(
    game_env: tuple[Surface, Settings],
) -> None:
    """Testa movimentação do Alien padrão utilizando Fixture."""
    screen, settings = game_env
    alien = Alien(screen, settings)
    x_inicial = alien.x

    alien.update()

    assert alien.x == pytest.approx(x_inicial + settings.alien_speed)


def test_fast_alien_doubles_speed_with_fixture(
    game_env: tuple[Surface, Settings],
) -> None:
    """Testa se o FastAlien move o dobro da velocidade do Alien comum."""
    screen, settings = game_env
    fast_alien = FastAlien(screen, settings)
    x_inicial = fast_alien.x

    fast_alien.update()

    assert fast_alien.x == pytest.approx(x_inicial + (settings.alien_speed * 2))


@pytest.mark.parametrize(
    ("steps", "expected_delta"),
    [
        (1, 1.0),
        (5, 5.0),
        (10, 10.0),
    ],
)
def test_bullet_upward_movement_parametrized(
    game_env: tuple[Surface, Settings],
    steps: int,
    expected_delta: float,
) -> None:
    """Testa o deslocamento vertical do projétil usando Parametrize."""
    screen, settings = game_env
    ship = Ship(screen, settings)
    bullet = Bullet(screen, settings, ship)
    y_inicial = bullet.y

    for _ in range(steps):
        bullet.update()

    assert bullet.y == pytest.approx(y_inicial - expected_delta)
