# How Many Pools in São Paulo?

Solution for the **Nimbus Level 3** challenge by [CloudWalk](https://nimbus.cloudwalk.io/).

Estimates the total number of swimming pools in São Paulo by combining computer vision detection (YOLOv8) with statistical extrapolation over satellite imagery.

## Pipeline

```
Sample locations (SP bounding box)
        ↓
Download tiles via Google Maps Static API
        ↓
Fine-tune YOLOv8 on pool dataset (Roboflow)
        ↓
Batch inference → pool count per image
        ↓
Statistical extrapolation → total estimate + 95% CI
        ↓
Interactive Folium map (heatmap + choropleth by district)
```

## Expected Results

| Metric | Target |
|---|---|
| mAP@0.5 | > 0.65 |
| Sample coverage | ~1,000 images |
| Output | `outputs/map.html` |

## Installation

```bash
pip install -r requirements.txt
cp .env.example .env
# fill in your API keys in .env
```

## Usage

```bash
# Full pipeline
python main.py --steps all

# Specific steps only
python main.py --steps collect detect estimate
```

## Project Structure

```
pools-sao-paulo/
├── src/
│   ├── collect.py    # location sampling + tile download
│   ├── train.py      # YOLOv8 fine-tuning
│   ├── detect.py     # batch inference
│   ├── estimate.py   # statistical extrapolation
│   └── visualize.py  # Folium map
├── data/
│   ├── raw/          # downloaded images (gitignored)
│   ├── labeled/      # training dataset (gitignored)
│   └── samples/      # sampled points (CSV)
├── models/           # trained weights (gitignored)
├── outputs/          # results (gitignored)
├── main.py
└── requirements.txt
```

## Required API Keys

- `GOOGLE_MAPS_API_KEY` — [Google Cloud Console](https://console.cloud.google.com/) → Maps Static API
- `ROBOFLOW_API_KEY` — [Roboflow](https://roboflow.com/) → pool dataset
