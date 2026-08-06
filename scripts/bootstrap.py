"""
Artha Bootstrap Script

Purpose:
    Initialize the project structure for Artha.

Usage:
    python scripts/bootstrap.py
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


FOLDERS = [
    # Documentation
    "docs/foundation",
    "docs/prd",
    "docs/edr",

    # Data
    "data/raw",
    "data/interim",
    "data/processed",
    "data/external",

    # Notebooks
    "notebooks/exploratory",
    "notebooks/experiments",

    # Source Code
    "src/artha",
    "src/artha/config",
    "src/artha/ingestion",
    "src/artha/validation",
    "src/artha/processing",
    "src/artha/analytics",
    "src/artha/visualization",
    "src/artha/utils",
    "src/artha/pipelines",
    "src/artha/storage",

    # Tests
    "tests",

    # Assets
    "assets/images",
    "assets/diagrams",
]


INIT_FILES = [
    "src/artha/__init__.py",
]


def create_folder(path: Path) -> None:
    """Create a folder if it doesn't already exist."""
    path.mkdir(parents=True, exist_ok=True)


def create_file(path: Path) -> None:
    """Create an empty file if it doesn't already exist."""
    if not path.exists():
        path.touch()


def create_gitkeep(folder: Path) -> None:
    """
    Create a .gitkeep file inside the folder
    so Git tracks empty directories.
    """
    gitkeep = folder / ".gitkeep"

    if not gitkeep.exists():
        gitkeep.touch()


def main() -> None:

    print("=" * 60)
    print("Bootstrapping Artha...")
    print("=" * 60)

    for folder in FOLDERS:

        folder_path = PROJECT_ROOT / folder

        create_folder(folder_path)
        create_gitkeep(folder_path)

        print(f"[✓] Folder : {folder}")

    for file in INIT_FILES:

        file_path = PROJECT_ROOT / file

        create_file(file_path)

        print(f"[✓] File   : {file}")

    print("\nProject structure created successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()