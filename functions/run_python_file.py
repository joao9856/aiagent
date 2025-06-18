import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    try:
        wkd = os.path.abspath(working_directory)
        file = os.path.abspath(os.path.join(working_directory, file_path))
        if file.startswith(wkd) == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if os.path.exists(file) == False:
            return f'Error: File "{file_path}" not found.'
        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file.'
        output = subprocess.run(["python3", file], timeout=30, capture_output=True, text=True, cwd=wkd)
        formated = []
        if output.stdout:
            formated.append(f"STDOUT:\n{output.stdout}")
        if output.stderr:
            formated.append(f"STDERR:\n{output.stderr}")
        if output.returncode != 0:
            formated = f"{formated}\nProcess exited with code {output.returncode}"
        if output:
            return "\n".join(formated)
        return "No output produced"
    except Exception as error:
        return f"Error: executing Python file: {error}"


schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Runs a python file, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file to run, relative to the working directory.",
                ),
            },
        ),
    )