
import subprocess
import sys


def run(command: list[str]) -> None:
    print(f"Running: {' '.join(command)}")

    subprocess.run(
        command,
        check=True,
    )


def main():
    python = sys.executable

    run([
        python,
        "mlops/data/generate_data.py",
    ])

    run([
        python,
        "mlops/preprocessing/prepare.py",
    ])

    run([
        python,
        "mlops/training/train.py",
    ])

    print("MLOps training pipeline completed.")


if __name__ == "__main__":
    main()
