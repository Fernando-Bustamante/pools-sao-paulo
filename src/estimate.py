"""
Extrapolação estatística para estimar o total de piscinas em São Paulo.

Conceito:
  - Cada imagem amostrada cobre ~0.03 km² (640px @ zoom 19, lat -23.5°)
  - SP tem ~1521 km² de área urbana
  - Densidade = piscinas_detectadas / área_amostrada (km²)
  - Estimativa total = densidade × área_total

Método de amostragem estratificada (bônus):
  - Divide SP em estratos por tipo de ocupação (alta renda, baixa renda, industrial)
  - Amostra proporcionalmente em cada estrato
  - Reduz a variância da estimativa

Outputs:
  - Estimativa pontual (número total)
  - Intervalo de confiança 95%
  - Tabela por distrito
"""

SP_AREA_KM2 = 1521.11
IMAGE_AREA_KM2 = 0.0307  # área coberta por tile 640px zoom=19 em lat=-23.5°


def load_predictions(predictions_dir: str) -> list[dict]:
    """Carrega todos os JSONs de detecção e retorna lista de resultados."""
    pass


def compute_density(predictions: list[dict]) -> float:
    """Calcula piscinas por km² com base nas imagens amostradas."""
    pass


def extrapolate(density: float, city_area: float = SP_AREA_KM2) -> float:
    """Multiplica densidade pela área total da cidade."""
    pass


def confidence_interval(predictions: list[dict], confidence: float = 0.95) -> tuple[float, float]:
    """Retorna intervalo de confiança via bootstrap."""
    pass


def by_district(predictions: list[dict]) -> dict:
    """Agrupa estimativas por distrito usando shapefiles do IBGE."""
    pass


def run(predictions_dir: str = "outputs/predictions") -> None:
    """Ponto de entrada: carrega predições, calcula e imprime estimativa final."""
    pass
