import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
VENV_DIR = ROOT / ".venv"
VENV_PYTHON = VENV_DIR / "Scripts" / "python.exe" if os.name == "nt" else VENV_DIR / "bin" / "python"


# -----------------------------
# Utilities
# -----------------------------

def run(cmd, cwd=None):
    print(f"\n>>> {' '.join(map(str, cmd))}")
    result = subprocess.run(cmd, cwd=cwd)
    if result.returncode != 0:
        sys.exit(result.returncode)


def safe_rmtree(path):
    if path.exists():
        print(f"Removing {path}")
        shutil.rmtree(path, ignore_errors=True)


def copy_tree(src, dst):
    if src.exists():
        shutil.copytree(src, dst, dirs_exist_ok=True)


# -----------------------------
# Tasks
# -----------------------------

def cleanup():
    safe_rmtree(ROOT / "result")
    safe_rmtree(ROOT / "build")
    safe_rmtree(ROOT / "dist")
    safe_rmtree(ROOT / "keywords")
    safe_rmtree(ROOT / "robotframework_flaui.egg-info")


def venv():
    if not VENV_DIR.exists():
        run([sys.executable, "-m", "venv", str(VENV_DIR)])

    run([str(VENV_PYTHON), "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])
    run([str(VENV_PYTHON), "-m", "pip", "install", "-r", "requirements-dev.txt"])


def build():
    cleanup()
    venv()
    run([str(VENV_PYTHON), "-m", "build"])
    run([str(VENV_PYTHON), "libdoc.py"])


def install():
    build()
    run([str(VENV_PYTHON), "-m", "pip", "install", "."])


def test_uia2():
    run([
        str(VENV_PYTHON),
        "-m", "robot",
        "--name", "UIA2",
        "--variable", "UIA:UIA2",
        "--outputdir", "../result/uia2",
        "."
    ], cwd=ROOT / "atests")


def test_uia3():
    run([
        str(VENV_PYTHON),
        "-m", "robot",
        "--name", "UIA3",
        "--variable", "UIA:UIA3",
        "--outputdir", "../result/uia3",
        "."
    ], cwd=ROOT / "atests")


def pylint():
    (ROOT / "result").mkdir(exist_ok=True)
    run([str(VENV_PYTHON), "-m", "pylint", "src"])


def robocop():
    run([str(VENV_PYTHON), "robocop_lint.py"])


def test():
    install()
    robocop()
    pylint()
    test_uia2()
    test_uia3()

    run([
        str(VENV_PYTHON),
        "-m", "robot.rebot",
        "--name", "ATests",
        "--outputdir", "result",
        "-x", "rebot_xunit.xml",
        "result/uia2/output.xml",
        "result/uia3/output.xml",
    ])

    # Merge screenshots
    copy_tree(ROOT / "result/uia2/screenshots", ROOT / "result/screenshots")
    copy_tree(ROOT / "result/uia3/screenshots", ROOT / "result/screenshots")

    for path in (ROOT / "result/uia2").rglob("*.jpg"):
        shutil.copy(path, ROOT / "result")

    for path in (ROOT / "result/uia3").rglob("*.jpg"):
        shutil.copy(path, ROOT / "result")

    run([str(VENV_PYTHON), "parsly.py"])


# -----------------------------
# CLI Dispatcher
# -----------------------------

TASKS = {
    "cleanup": cleanup,
    "venv": venv,
    "build": build,
    "install": install,
    "test": test,
    "test_uia2": test_uia2,
    "test_uia3": test_uia3,
    "pylint": pylint,
    "robocop": robocop,
}

if __name__ == "__main__":
    print("Running:", __file__)
    print("Args:", sys.argv)

    if len(sys.argv) < 2:
        print(f"Available tasks: {', '.join(TASKS)}")
        sys.exit(1)

    task = sys.argv[1]

    if task not in TASKS:
        print(f"Unknown task: {task}")
        sys.exit(1)

    TASKS[task]()
