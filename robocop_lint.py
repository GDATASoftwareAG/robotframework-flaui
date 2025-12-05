import sys
import subprocess

# Different calls between python 3.8 usage .robocop file and 3.9++ robocop.toml
py_ver = sys.version_info

if py_ver < (3, 9):
    cmd = [sys.executable, "-m", "robocop", "atests", "--configure", "return_status:quality_gate:E=0:W=0:I=0"]
else:
    cmd = [sys.executable, "-m", "robocop", "check"]

result = subprocess.run(cmd)
sys.exit(result.returncode)
