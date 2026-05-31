"""
Geração do mapa interativo de densidade de piscinas em São Paulo.

Outputs:
  - outputs/map.html — mapa Folium com:
      * Heatmap de densidade de piscinas
      * Choropleth por distrito (comparação entre regiões)
      * Marcadores clicáveis nas imagens amostradas

Dados necessários:
  - outputs/predictions/*.json  (gerado por detect.py)
  - Shapefile de distritos de SP (IBGE, baixado automaticamente)
"""

SP_CENTER = (-23.5505, -46.6333)
IBGE_DISTRICTS_URL = "https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2022/UFs/SP/"


def load_district_shapes(shapefile_path: str):
    """Carrega GeoDataFrame com os polígonos dos distritos de SP."""
    pass


def build_heatmap(predictions: list[dict]):
    """Cria mapa Folium com camada de heatmap sobre as localizações amostradas."""
    pass


def add_choropleth(folium_map, district_counts: dict, shapes):
    """Adiciona camada choropleth com densidade por distrito."""
    pass


def add_sample_markers(folium_map, predictions: list[dict]) -> None:
    """Adiciona marcadores clicáveis para amostras com piscinas detectadas."""
    pass


def run(predictions_dir: str = "outputs/predictions", output_path: str = "outputs/map.html") -> None:
    """Ponto de entrada: gera e salva o mapa completo."""
    pass
