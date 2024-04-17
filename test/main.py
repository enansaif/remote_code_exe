import subprocess
import sys
print(f"current venv ->{sys.prefix}")

subprocess.run("python -m venv .rce", shell=True)
output = subprocess.run(".rce/bin/python script.py", shell=True, capture_output=True, text=True)
subprocess.run("rm -r .rce", shell=True)

if output.stdout:
    print(f"stdout\n{output.stdout}")

if output.returncode != 0:
    print(f"error\n{output.stderr}")