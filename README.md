# How Many Pools in São Paulo?

Solução para o desafio **Nimbus Level 3** da [CloudWalk](https://nimbus.cloudwalk.io/).

Estima o número total de piscinas em São Paulo combinando detecção por visão computacional (YOLOv8) com extrapolação estatística sobre imagens de satélite.

## Pipeline

```
Amostragem de localizações (SP bbox)
        ↓
Download de tiles via Google Maps Static API
        ↓
Fine-tune YOLOv8 em dataset de piscinas (Roboflow)
        ↓
Inferência em lote → contagem por imagem
        ↓
Extrapolação estatística → estimativa total + IC 95%
        ↓
Mapa Folium interativo (heatmap + choropleth por distrito)
```

## Resultado esperado

| Métrica | Meta |
|---|---|
| mAP@0.5 | > 0.65 |
| Cobertura amostral | ~1.000 imagens |
| Output | `outputs/map.html` |

## Instalação

```bash
pip install -r requirements.txt
cp .env.example .env
# preencha as chaves no .env
```

## Uso

```bash
# Pipeline completo
python main.py --steps all

# Apenas etapas específicas
python main.py --steps collect detect estimate
```

## Estrutura

```
pools-sao-paulo/
├── src/
│   ├── collect.py    # amostragem + download de tiles
│   ├── train.py      # fine-tune YOLOv8
│   ├── detect.py     # inferência em lote
│   ├── estimate.py   # extrapolação estatística
│   └── visualize.py  # mapa Folium
├── data/
│   ├── raw/          # imagens baixadas (gitignored)
│   ├── labeled/      # dataset de treino (gitignored)
│   └── samples/      # pontos amostrados (CSV)
├── models/           # pesos treinados (gitignored)
├── outputs/          # resultados (gitignored)
├── main.py
└── requirements.txt
```

## Chaves necessárias

- `GOOGLE_MAPS_API_KEY` — [Google Cloud Console](https://console.cloud.google.com/) → Maps Static API
- `ROBOFLOW_API_KEY` — [Roboflow](https://roboflow.com/) → dataset de piscinas
