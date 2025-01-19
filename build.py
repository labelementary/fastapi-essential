import subprocess


def build():
    # Run pre-commit hooks
    subprocess.run(["pre-commit", "run", "--all-files"], check=True)
