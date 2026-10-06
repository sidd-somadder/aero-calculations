import os
import shutil
import subprocess
import tempfile
import numpy as np

def find_xfoil():

    # check system environment variable 
    explicit = os.environ.get("XFOIL_PATH")
    if explicit and os.path.isfile(explicit):
        return explicit

    found = shutil.which("xfoil") or shutil.which("xfoil.exe")
    if found:
        return found

    for candidate in [os.path.expanduser(r"~\XFOIL6.99\xfoil.exe"),]:
        if os.path.isfile(candidate):
            return candidate

    raise FileNotFoundError("XFOIL not found")

print(find_xfoil())
    