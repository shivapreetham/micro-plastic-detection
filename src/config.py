import argparse
from pathlib import Path
import yaml


def load_config(config_path: str | Path) -> dict:
    config_path = Path(config_path)
    with config_path.open("r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    # Basic defaults
    cfg.setdefault("data", {})
    cfg.setdefault("train", {})
    cfg.setdefault("model", {})
    cfg.setdefault("augment", {})
    return cfg


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True, help="Path to YAML config")
    return parser.parse_args()

