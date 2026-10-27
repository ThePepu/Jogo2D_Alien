import pygame
from pytest_mock import MockerFixture

from src.alien_invasion import AlienInvasion
from src.game_events import GameEventHandler
from src.settings import Settings
from src.ship import Ship
from tests.doubles import StubBulletManager, StubFleetManager


def test_event_handler_spacebar_with_stub() -> None:
    """Testa o disparo na tecla ESPAÇO usando um Stub de IBulletManager."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    settings = Settings()
    ship = Ship(screen, settings)
    stub_bullets = StubBulletManager()

    handler = GameEventHandler(ship, stub_bullets)
    event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
    handler._handle_keydown(event)

    assert stub_bullets.fired_count == 1


def test_alien_invasion_update_state_with_stubs() -> None:
    """Testa _update_game_state isoladamente injetando Stubs nas dependências."""
    stub_bullets = StubBulletManager()
    stub_fleet = StubFleetManager()

    game = AlienInvasion(
        bullet_manager=stub_bullets,
        fleet_manager=stub_fleet,
    )
    game._update_game_state()

    assert stub_bullets.updated_count == 1
    assert stub_fleet.updated_count == 1


def test_event_handler_with_mock_bullet_manager(mocker: MockerFixture) -> None:
    """Testa a interação do GameEventHandler usando Mock (pytest-mock)."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    settings = Settings()
    ship = Ship(screen, settings)

    mock_bullet_manager = mocker.Mock()
    handler = GameEventHandler(ship, mock_bullet_manager)

    event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
    handler._handle_keydown(event)

    mock_bullet_manager._fire_bullet.assert_called()
    mock_bullet_manager._fire_bullet.assert_called_once_with()
    assert mock_bullet_manager._fire_bullet.call_count == 1


def test_alien_invasion_update_with_mocks(mocker: MockerFixture) -> None:
    """Verifica a chamada e os argumentos de atualização usando Mocks."""
    mock_bullets = mocker.Mock()
    mock_bullets.bullets = pygame.sprite.Group()

    mock_fleet = mocker.Mock()
    mock_fleet.aliens = pygame.sprite.Group()

    game = AlienInvasion(
        bullet_manager=mock_bullets,
        fleet_manager=mock_fleet,
    )
    game._update_game_state()

    mock_bullets._update_bullets.assert_called_once_with(mock_fleet.aliens)
    mock_fleet._update_aliens.assert_called_once()
