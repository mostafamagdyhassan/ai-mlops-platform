
import json
from pathlib import Path


def evaluate_response(
    response: str,
    required_sections: list[str],
) -> dict:

    normalized = response.lower()

    checks = {
        section: section.lower() in normalized
        for section in required_sections
    }

    passed = sum(checks.values())

    return {
        "passed_checks": passed,
        "total_checks": len(checks),
        "score": passed / len(checks) if checks else 0,
        "checks": checks,
    }


def save_evaluation(result: dict, output: str):
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    sample = """
    Incident summary:
    Possible root causes:
    Technical evidence:
    Recommended investigation steps:
    Suggested remediation:
    Potential impact:
    Confidence level:
    """

    sections = [
        "Incident summary",
        "Possible root causes",
        "Technical evidence",
        "Recommended investigation steps",
        "Suggested remediation",
        "Potential impact",
        "Confidence level",
    ]

    result = evaluate_response(sample, sections)

    save_evaluation(
        result,
        "mlops/evaluation/ai_evaluation.json",
    )

    print(json.dumps(result, indent=2))
