
$ErrorActionPreference = "Stop"

if (-not (Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
    Write-Host "Created .env file."
}

docker compose up -d postgres qdrant

if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install -e ".[dev,ml,ai]"

Write-Host "Local dependencies are ready."
Write-Host "Start the API with:"
Write-Host "uvicorn application.main:app --reload"
