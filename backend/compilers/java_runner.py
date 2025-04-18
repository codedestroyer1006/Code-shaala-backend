import subprocess
import os
import uuid
import re

def run_java(code):
    file_id = str(uuid.uuid4().hex)
    class_name = "Main"
    java_filename = f"{class_name}.java"
    java_filepath = f"/tmp/{java_filename}"
    class_file = f"/tmp/{class_name}.class"

    # Extract the original class name
    class_match = re.search(r'public\s+class\s+(\w+)', code)
    if not class_match:
        return {"error": "❌ No public class found in the code."}
    
    original_class_name = class_match.group(1)

    # Rename the original class name to 'Main'
    code = code.replace(f'public class {original_class_name}', f'public class {class_name}', 1)

    # Clean old files
    if os.path.exists(java_filepath):
        os.remove(java_filepath)
    if os.path.exists(class_file):
        os.remove(class_file)

    # Write updated code
    with open(java_filepath, "w") as f:
        f.write(code)

    try:
        # Compile
        compile = subprocess.run(["javac", java_filepath], capture_output=True, text=True)
        if compile.returncode != 0:
            return {"error": compile.stderr.strip()}

        # Run
        run = subprocess.run(["java", "-cp", "/tmp", class_name], capture_output=True, text=True)
        if run.returncode != 0:
            return {"error": run.stderr.strip()}

        return {"output": run.stdout.strip()}
    except Exception as e:
        return {"error": str(e)}
