class Settings:
    """Classe que armazena todas as configurações do jogo."""

    def __init__(self) -> None:
        # Configurações da tela
        self.screen_width: int = 1200
        self.screen_height: int = 800
        self.bg_color: tuple[int, int, int] = (
            230,
            230,
            230,
        )  # Cor de fundo (cinza claro)
        self.ship_speed: float = 1.5  # Velocidade da nave

        # Configurações dos projéteis
        self.bullet_speed: float = 1.0  # Velocidade dos projéteis
        self.bullet_width: int = 3  # Largura dos projéteis
        self.bullet_height: int = 15  # Altura dos projéteis
        self.bullet_color: tuple[int, int, int] = (60, 60, 60)  # Cor dos projeteis
        self.bullet_allowed: int = (
            1  # Número máximo de projéteis que podem existir na tela ao mesmo tempo
        )

        # Configurações do alien
        self.alien_speed: float = 0.3  # Velocidade dos alienígenas
        self.fleet_drop_speed: int = (
            10  # Velocidade com que a frota de alienígenas desce em direção à nave
        )
        self.fleet_direction: int = 1  # Direção da frota de alienígenas: 1 representa a direita; -1 representa a esquerda
