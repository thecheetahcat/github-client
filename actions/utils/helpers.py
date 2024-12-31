import subprocess
from typing import Optional


def run_command(command: str, capture_output: bool = False) -> Optional[str]:
    try:
        if capture_output:
            return subprocess.run(
                command,
                shell=True,
                check=True,
                capture_output=True,
                text=True
            ).stdout
        else:
            subprocess.run(
                command,
                shell=True,
                check=True
            )
            return None
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
