
import numpy as np
from sklearn.ensemble import IsolationForest


def test_isolation_forest_detects_extreme_anomaly():
    rng = np.random.default_rng(42)

    normal = rng.normal(
        loc=50,
        scale=5,
        size=(200, 4),
    )

    anomalies = np.array([
        [100, 100, 100, 100]
    ])

    model = IsolationForest(
        contamination=0.05,
        random_state=42,
    )

    model.fit(normal)

    prediction = model.predict(anomalies)

    assert prediction[0] == -1
