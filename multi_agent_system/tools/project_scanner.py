from pathlib import Path


IGNORED_DIRS = {".git", "__pycache__", ".pytest_cache", "venv", ".venv", "runs"}


def scan_project(root: Path) -> dict:
    """Scan a project directory and return lightweight statistics."""

    root = root.resolve()
    total_files = 0
    python_files = 0
    markdown_files = 0
    test_files = 0
    top_level = []

    if not root.exists():
        return {
            "root": str(root),
            "exists": False,
            "total_files": 0,
            "python_files": 0,
            "markdown_files": 0,
            "test_files": 0,
            "top_level": [],
        }

    for item in root.iterdir():
        if item.name not in IGNORED_DIRS:
            top_level.append(item.name)

    for path in root.rglob("*"):
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        if path.is_file():
            total_files += 1
            if path.suffix == ".py":
                python_files += 1
            if path.suffix.lower() in {".md", ".markdown"}:
                markdown_files += 1
            if path.name.startswith("test_") and path.suffix == ".py":
                test_files += 1

    return {
        "root": str(root),
        "exists": True,
        "total_files": total_files,
        "python_files": python_files,
        "markdown_files": markdown_files,
        "test_files": test_files,
        "top_level": sorted(top_level)[:20],
    }
