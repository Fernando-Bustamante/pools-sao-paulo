"""
Inferência em lote nas imagens amostradas de São Paulo.

Fluxo:
  1. load_model()     — carrega pesos YOLOv8 treinados
  2. detect_image()   — roda detecção em uma imagem, retorna lista de bboxes
  3. run()            — processa todo data/raw/, salva resultados em outputs/predictions/

Formato de saída por imagem (JSON):
  {
    "image": "filename.jpg",
    "lat": -23.55,
    "lon": -46.63,
    "pools_detected": 3,
    "detections": [{"bbox": [x1,y1,x2,y2], "conf": 0.87}, ...]
  }
"""

DEFAULT_CONF = 0.40


def load_model(weights_path: str):
    """Carrega e retorna modelo YOLOv8 a partir dos pesos salvos."""
    pass


def detect_image(model, image_path: str, conf: float = DEFAULT_CONF) -> dict:
    """Roda inferência em uma imagem e retorna dict com contagem e bboxes."""
    pass


def run(images_dir: str = "data/raw", weights: str = "models/best.pt", output_dir: str = "outputs/predictions") -> None:
    """Ponto de entrada: inferência em lote em todas as imagens."""
    pass
