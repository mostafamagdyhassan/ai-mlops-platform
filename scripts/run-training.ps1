
$ErrorActionPreference = "Stop"

Write-Host "Starting ML training pipeline..."

python mlops/data/generate_data.py

python mlops/preprocessing/prepare.py

python mlops/pipelines/run_training.py

Write-Host "Training pipeline completed."
