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
    output_path: str = None,
    include_metadata: bool = True,
) -> Path:
    """Formats and writes the evaluation report to disk with the repository name in the filename."""
    cleaned_report = clean_markdown_output(raw_report)

    # 1. Extract the repository name (e.g., 'owner/repo-name' -> 'repo-name')
    full_repo = os.environ.get("GITHUB_REPOSITORY", "local_repository")
    repo_name = full_repo.split("/")[-1] if "/" in full_repo else full_repo

    # 2. Dynamically set the output path if not explicitly provided
    if output_path is None or output_path == "evaluation_reports/evaluation_report.md":
        output_path = f"evaluation_reports/{repo_name}_evaluation_report.md"

    final_content = cleaned_report
    if include_metadata:
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        commit_sha = os.environ.get("GITHUB_SHA", "N/A")[:7]

        metadata_banner = (
            f"> **Automated AI Evaluation Metadata**  \n"
            f"> **Repository:** `{full_repo}` | **Commit:** `{commit_sha}` | **Generated:** {timestamp}\n\n"
            f"---\n\n"
        )
        final_content = metadata_banner + cleaned_report

    out_file = Path(output_path)

    # If only a filename was passed, force it into evaluation_reports/
    if out_file.parent == Path("."):
        out_file = Path("evaluation_reports") / out_file.name

    # Automatically creates the 'evaluation_reports' directory if it doesn't exist
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(final_content, encoding="utf-8")

    return out_file.resolve()
