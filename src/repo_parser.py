import os
from pathlib import Path

EXCLUDE_DIRS = {".git", "__pycache__", "venv", ".venv", "node_modules", "artifacts"}
SUPPORTED_EXTENSIONS = {".py", ".ipynb", ".md", ".txt", ".yaml", ".yml"}


def parse_repository(repo_path: str) -> dict:
    codebase_content = {}
    root_path = Path(repo_path)

    for file_path in root_path.rglob("*"):
        if any(part in EXCLUDE_DIRS for part in file_path.parts):
            continue
        if file_path.is_file() and file_path.suffix in SUPPORTED_EXTENSIONS:
            relative_path = str(file_path.relative_to(root_path))
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    codebase_content[relative_path] = f.read()
            except Exception as e:
                codebase_content[relative_path] = f"# Error reading file: {e}"

    return codebase_content
