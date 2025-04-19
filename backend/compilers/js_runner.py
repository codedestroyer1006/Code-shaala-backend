import subprocess
import uuid
import os

def run_js(code):
    file_id = uuid.uuid4().hex
    filename = f"/tmp/{file_id}.js"

    with open(filename, "w") as f:
        f.write(code)

    try:
        result = subprocess.run(
            ["node", filename], capture_output=True, text=True, timeout=5
        )

        return {
            "output": result.stdout.strip(),
            "error": result.stderr.strip() if result.returncode != 0 else ""
        }
    except FileNotFoundError:
        return {"error": "Node.js is not installed on the server."}
    except subprocess.TimeoutExpired:
        return {"error": "Execution timed out."}
    finally:
        os.remove(filename)
