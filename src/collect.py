"""
Coleta de imagens de satélite de São Paulo via Google Maps Static API.

Fluxo:
  1. sample_locations()  — sorteia N pontos aleatórios dentro do bbox de SP
  2. download_tile()     — baixa uma imagem 640x640 (zoom 19) para cada ponto
  3. run()               — orquestra os dois passos e salva em data/raw/

O bbox de São Paulo (cidade):
  lat: -24.008 a -23.357
  lon: -46.826 a -46.365
"""

SP_BBOX = {
    "lat_min": -24.008,
    "lat_max": -23.357,
    "lon_min": -46.826,
    "lon_max": -46.365,
}

ZOOM = 19
IMG_SIZE = 640  # pixels


def sample_locations(n: int, bbox: dict = SP_BBOX) -> list[tuple[float, float]]:
    """Sorteia n pares (lat, lon) uniformemente dentro do bbox."""
    pass


def download_tile(lat: float, lon: float, zoom: int, api_key: str, output_path: str) -> None:
    """Baixa tile de satélite via Google Maps Static API e salva como JPEG."""
    pass


def run(n_samples: int = 1000, output_dir: str = "data/raw") -> None:
    """Ponto de entrada: amostra localizações e baixa as imagens."""
    pass
