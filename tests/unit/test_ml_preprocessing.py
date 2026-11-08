
import pandas as pd
import pytest

from mlops.preprocessing.prepare import FEATURES


def test_required_features_are_defined():
    assert "cpu_usage" in FEATURES
    assert "memory_usage" in FEATURES
    assert "disk_usage" in FEATURES
    assert "network_traffic" in FEATURES


def test_feature_values_are_numeric():
    data = pd.DataFrame({
        "cpu_usage": [50.0],
        "memory_usage": [60.0],
        "disk_usage": [40.0],
        "network_traffic": [100.0],
    })

    assert all(
        pd.api.types.is_numeric_dtype(data[column])
        for column in FEATURES
    )
