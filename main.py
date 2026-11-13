import argparse
from pathlib import Path
from src.repo_parser import parse_repository
from src.code_analyser import generate_evaluation_report
from src.report_generator import save_evaluation_report


def main():
    parser = argparse.ArgumentParser(description="AI Agent Repo Reviewer")
    parser.add_argument(
        "--repo-path", type=str, default=".", help="Path to the repository to analyze"
    )
    parser.add_argument(
        "--output", type=str, default="evaluation_report.md", help="Output report path"
    )
    parser.add_argument(
        "--model", type=str, default="gemini-3.8-flash", help="Gemini model name"
    )
    args = parser.parse_args()

    print(f"Scanning repository at: {args.repo_path}")
    codebase = parse_repository(args.repo_path)

    prompt_path = Path("prompts/evaluation_system_prompt.md")
    system_prompt = prompt_path.read_text(encoding="utf-8")

    print(f"Sending {len(codebase)} files to {args.model} for evaluation...")
    raw_report = generate_evaluation_report(
        codebase, system_prompt, model_name=args.model
    )

    saved_path = save_evaluation_report(raw_report, output_path=args.output)
    print(f"Report successfully generated and saved to: {saved_path}")


if __name__ == "__main__":
    main()
