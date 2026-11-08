
import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def generate_metrics(samples: int = 5000) -> pd.DataFrame:
    rng = np.random.default_rng(42)

    cpu = rng.normal(45, 12, samples).clip(1, 100)
    memory = rng.normal(55, 10, samples).clip(1, 100)
    disk = rng.normal(50, 15, samples).clip(1, 100)
    network = rng.normal(100, 30, samples).clip(1, 1000)

    normal_data = pd.DataFrame({
        "cpu_usage": cpu,
        "memory_usage": memory,
        "disk_usage": disk,
        "network_traffic": network,
        "is_anomaly": 0,
    })

    anomaly_count = max(1, samples // 20)

    anomalies = pd.DataFrame({
        "cpu_usage": rng.uniform(90, 100, anomaly_count),
        "memory_usage": rng.uniform(90, 100, anomaly_count),
        "disk_usage": rng.uniform(85, 100, anomaly_count),
        "network_traffic": rng.uniform(700, 1000, anomaly_count),
        "is_anomaly": 1,
    })

    return pd.concat(
        [normal_data, anomalies],
        ignore_index=True,
    ).sample(frac=1, random_state=42).reset_index(drop=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=5000)
    parser.add_argument(
        "--output",
        default="mlops/data/infrastructure_metrics.csv",
    )
    args = parser.parse_args()

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    data = generate_metrics(args.samples)
    data.to_csv(output, index=False)

    print(f"Generated {len(data)} records: {output}")


if __name__ == "__main__":
    main()
