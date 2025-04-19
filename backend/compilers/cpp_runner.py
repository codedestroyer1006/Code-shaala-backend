import subprocess
import os
import uuid

def run_cpp(code, user_input=""):
    unique_id = uuid.uuid4().hex
    filename = f"/tmp/program_{unique_id}.cpp"
    output_file = f"/tmp/program_{unique_id}"

    try:
        # Write the C++ code to a file
        with open(filename, "w") as f:
            f.write(code)

        # Compile the C++ file
        compile_process = subprocess.run(
            ["g++", filename, "-o", output_file],
            capture_output=True,
            text=True
        )

        if compile_process.returncode != 0:
            return {"error": compile_process.stderr}

        # Run the compiled executable
        run_process = subprocess.run(
            [output_file],
            input=user_input,
            capture_output=True,
            text=True,
            timeout=5
        )

        return {
            "output": run_process.stdout.strip(),
            "error": run_process.stderr.strip() if run_process.returncode != 0 else ""
        }

    except subprocess.TimeoutExpired:
        return {"error": "Execution timed out."}
    except Exception as e:
        return {"error": str(e)}
    finally:
        # Clean up temporary files
        if os.path.exists(filename):
            os.remove(filename)
        if os.path.exists(output_file):
            os.remove(output_file)
