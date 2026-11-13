import os
from datetime import datetime, timezone
from pathlib import Path


def clean_markdown_output(raw_text: str) -> str:
    """Strips outer ```markdown ... ``` wrappers if the LLM included them."""
    text = raw_text.strip()
    if text.startswith("```markdown"):
        text = text[len("```markdown") :].strip()
    elif text.startswith("```"):
        text = text[3:].strip()

    if text.endswith("```"):
        text = text[:-3].strip()

    return text


def save_evaluation_report(
    raw_report: str,
    output_path: str = "evaluation_reports/evaluation_report.md",
    include_metadata: bool = True,
) -> Path:
    """Formats and writes the evaluation report to the evaluation_reports folder."""
    cleaned_report = clean_markdown_output(raw_report)

    final_content = cleaned_report
    if include_metadata:
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        repo_name = os.environ.get("GITHUB_REPOSITORY", "Local Repository")
        commit_sha = os.environ.get("GITHUB_SHA", "N/A")[:7]

        metadata_banner = (
            f"> **Automated AI Evaluation Metadata**  \n"
            f"> **Repository:** `{repo_name}` | **Commit:** `{commit_sha}` | **Generated:** {timestamp}\n\n"
            f"---\n\n"
        )
        final_content = metadata_banner + cleaned_report

    out_file = Path(output_path)

    # If only a filename was passed instead of a path, force it into evaluation_reports/
    if out_file.parent == Path("."):
        out_file = Path("evaluation_reports") / out_file.name

    # Automatically creates the 'evaluation_reports' directory if it doesn't exist
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(final_content, encoding="utf-8")

    return out_file.resolve()
