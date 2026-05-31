"""
Fine-tune YOLOv8 para detecção de piscinas em imagens de satélite.

Fluxo:
  1. download_dataset()  — baixa dataset anotado do Roboflow (formato YOLO)
  2. train()             — treina YOLOv8n/s com os dados baixados
  3. evaluate()          — calcula mAP@0.5 no conjunto de validação
                           (meta do desafio: mAP > 0.65)

Dataset recomendado (Roboflow Universe):
  "Swimming Pool Detection" — imagens aéreas com bboxes de piscinas.
"""

BASE_MODEL = "yolov8n.pt"
TARGET_MAP = 0.65


def download_dataset(roboflow_key: str, workspace: str, project: str, version: int, output_dir: str = "data/labeled") -> str:
    """Baixa dataset do Roboflow e retorna o caminho do data.yaml."""
    pass


def train(data_yaml: str, base_model: str = BASE_MODEL, epochs: int = 50, output_dir: str = "models") -> str:
    """Treina YOLOv8 e retorna o caminho dos pesos treinados (best.pt)."""
    pass


def evaluate(weights_path: str, data_yaml: str) -> dict:
    """Avalia o modelo e retorna dict com mAP@0.5 e mAP@0.5:0.95."""
    pass


def run() -> None:
    """Ponto de entrada: baixa dataset, treina e avalia."""
    pass
