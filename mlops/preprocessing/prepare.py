
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


FEATURES = [
    "cpu_usage",
    "memory_usage",
    "disk_usage",
    "network_traffic",
]


def prepare_dataset(input_path: str, output_dir: str) -> None:
    data = pd.read_csv(input_path)

    required_columns = FEATURES + ["is_anomaly"]

    missing = set(required_columns) - set(data.columns)

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    data = data.dropna(subset=required_columns)

    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    train, test = train_test_split(
        data,
        test_size=0.2,
        random_state=42,
        stratify=data["is_anomaly"],
    )

    train.to_csv(output / "train.csv", index=False)
    test.to_csv(output / "test.csv", index=False)

    print(f"Training records: {len(train)}")
    print(f"Testing records: {len(test)}")


if __name__ == "__main__":
    prepare_dataset(
        "mlops/data/infrastructure_metrics.csv",
        "mlops/data/processed",
    )
