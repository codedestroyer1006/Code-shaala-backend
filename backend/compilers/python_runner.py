<<<<<<< HEAD
import subprocess
import os
import uuid

def run_python(code, user_input=""):
    filename = f"script_{uuid.uuid4().hex}.py"

    try:
        with open(filename, "w") as f:
            f.write(code)

        process = subprocess.run(
            ["python", filename],
            input=user_input,
            capture_output=True,
            text=True,
            timeout=5
        )

        return {
            "output": process.stdout.strip(),
            "error": process.stderr.strip() if process.returncode != 0 else ""
        }
    except subprocess.TimeoutExpired:
        return {"error": "Execution timed out"}
    finally:
        os.remove(filename)
=======
import subprocess
import os
import uuid

def run_python(code, user_input=""):
    filename = f"script_{uuid.uuid4().hex}.py"

    try:
        with open(filename, "w") as f:
            f.write(code)

        process = subprocess.run(
            ["python", filename],
            input=user_input,
            capture_output=True,
            text=True,
            timeout=5
        )

        return {
            "output": process.stdout.strip(),
            "error": process.stderr.strip() if process.returncode != 0 else ""
        }
    except subprocess.TimeoutExpired:
        return {"error": "Execution timed out"}
    finally:
        os.remove(filename)
>>>>>>> 1a0b9fd5c159a90b2daf2393fced31fb817d84c5
