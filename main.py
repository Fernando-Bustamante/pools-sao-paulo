"""
Pipeline completo: coleta → treino → detecção → estimativa → visualização.

Uso:
  python main.py --steps all
  python main.py --steps collect detect estimate
  python main.py --steps visualize

Passos disponíveis:
  collect   — baixa imagens de satélite (requer GOOGLE_MAPS_API_KEY)
  train     — treina YOLOv8 (requer ROBOFLOW_API_KEY)
  detect    — roda inferência nas imagens coletadas
  estimate  — calcula estimativa total + intervalo de confiança
  visualize — gera mapa Folium interativo
"""

import argparse
from dotenv import load_dotenv

load_dotenv()

STEPS = ["collect", "train", "detect", "estimate", "visualize"]


def parse_args():
    parser = argparse.ArgumentParser(description="How many pools in São Paulo?")
    parser.add_argument(
        "--steps",
        nargs="+",
        choices=STEPS + ["all"],
        default=["all"],
        help="Passos do pipeline a executar",
    )
    parser.add_argument("--n-samples", type=int, default=1000, help="Número de imagens a amostrar")
    return parser.parse_args()


def main():
    args = parse_args()
    steps = STEPS if "all" in args.steps else args.steps

    if "collect" in steps:
        from src.collect import run as collect
        collect(n_samples=args.n_samples)

    if "train" in steps:
        from src.train import run as train
        train()

    if "detect" in steps:
        from src.detect import run as detect
        detect()

    if "estimate" in steps:
        from src.estimate import run as estimate
        estimate()

    if "visualize" in steps:
        from src.visualize import run as visualize
        visualize()


if __name__ == "__main__":
    main()
