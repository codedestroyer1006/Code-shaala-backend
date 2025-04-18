import subprocess
import os
import uuid

def run_java(code):
    file_id = str(uuid.uuid4().hex)
    class_name = "Main"
    java_filename = f"{class_name}.java"
    java_filepath = f"/tmp/{java_filename}"
    class_file = f"/tmp/{class_name}.class"

    # Clean up any previous Main.java or Main.class to avoid stale code
    if os.path.exists(java_filepath):
        os.remove(java_filepath)
    if os.path.exists(class_file):
        os.remove(class_file)

    # Ensure class name is consistent
    if "public class" in code:
        code = code.replace("public class", f"public class {class_name}", 1)

    # Write the Java code to file
    with open(java_filepath, "w") as f:
        f.write(code)

    try:
        # Compile the Java file
        compile = subprocess.run(["javac", java_filepath], capture_output=True, text=True)
        if compile.returncode != 0:
            return {"error": compile.stderr.strip()}

        # Execute the compiled class
        run = subprocess.run(["java", "-cp", "/tmp", class_name], capture_output=True, text=True)
        if run.returncode != 0:
            return {"error": run.stderr.strip()}

        return {"output": run.stdout.strip()}
    except Exception as e:
        return {"error": str(e)}
