import subprocess
import os
import uuid

def run_java(code):
    file_id = str(uuid.uuid4().hex)
    filename = f"{file_id}.java"
    class_name = "Main"

    code = code.replace("public class", f"public class {class_name}")
    filepath = f"/tmp/{filename}"

    with open(filepath, "w") as f:
        f.write(code)

    try:
        # Compile
        compile = subprocess.run(["javac", filepath], capture_output=True, text=True)
        if compile.returncode != 0:
            return {"error": compile.stderr}

        # Execute
        run = subprocess.run(["java", "-cp", "/tmp", class_name], capture_output=True, text=True)
        return {"output": run.stdout or run.stderr}
    except Exception as e:
        return {"error": str(e)}
