import subprocess
import uuid
import os

def run_js(code):
    unique_id = uuid.uuid4().hex
    filename = f"/tmp/program_{unique_id}.js"

    try:
        with open(filename, "w") as f:
            f.write(code)

        run = subprocess.run(
            ["node", filename], capture_output=True, text=True, timeout=5
        )

        return {
            "output": run.stdout.strip(),
            "error": run.stderr.strip() if run.returncode != 0 else ""
        }
    except subprocess.TimeoutExpired:
        return {"error": "Execution timed out"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        if os.path.exists(filename):
            os.remove(filename)
