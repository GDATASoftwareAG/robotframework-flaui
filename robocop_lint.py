import sys
import subprocess

# Python 3.8 syntax does not support pyproject.toml syntax
# To support python 3.8 and newer builds we have to build a robocop.toml dynamically

include = [
  "atests",
]

py_ver = sys.version_info
if py_ver < (3, 9):
    robocop_ignore = [
        "0201", # Missing documentation in keyword
        "0202", # Missing documentation in test case
        "0204", # Missing documentation in resource file
        "0503", # Keyword has too many keywords inside
        "0504", # Test case is too long
        "0505", # Test case has too many keywords inside
        "0506", # File has to many lines
        "0508", # Line is too long
        "0527"  # Too many test cases
    ]
else:
    robocop_ignore = [
        "LEN03",   # Keyword has too many keywords inside
        "LEN04",   # Test case is too long
        "LEN06",   # Test case has too many keywords inside
        "LEN08",   # Line is too long
        "LEN27",   # Too many test cases
        "LEN28",   # File has to many lines
        "LEN32",   # Variable name is too long
        "DOC01",   # Missing documentation in keyword
        "DOC02",   # Missing documentation in test case
        "DOC04",   # Missing documentation in resource file
        "DEPR05",  # Set Variable used instead of VAR TODO -> Can be replaced in future
        "VAR04"    # Variable with global scope defined outside variables section
    ]

if py_ver < (3, 9):
    # Old robocop syntax
    if len(robocop_ignore) > 0:
        with open(".robocop", "w") as f:
            # Write tool robocop lint rules
            f.write("--exclude ")
            f.write(",".join(robocop_ignore))
else:
    # New robocop syntax
    with open("robocop.toml", "w") as f:
        # Write tool robocop lint rules
        f.write("[tool.robocop]\n")
        f.write("include = [\n")
        for rule in include:
            f.write(f'    "{rule}",\n')
        f.write("]\n")
        # Write tool robocop lint rules
        f.write("[tool.robocop.lint]\n")
        f.write("ignore = [\n")
        for rule in robocop_ignore:
            f.write(f'    "{rule}",\n')
        f.write("]\n")

if py_ver < (3, 9):
    cmd = [sys.executable, "-m", "robocop", "atests", "--configure", "return_status:quality_gate:E=0:W=0:I=0"]
else:
    cmd = [sys.executable, "-m", "robocop", "check"]

result = subprocess.run(cmd)
sys.exit(result.returncode)

