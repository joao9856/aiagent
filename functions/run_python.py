import os
import subprocess

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
        #return_code, stdout, stderr 
        output = subprocess.run(["python3", file], timeout=30, capture_output=True)
        output.stdout = f"STDOUT: {output.stdout}"
        output.stderr = f"STDERR: {output.stderr}"
        formated = f"{output.stdout}\n{output.stderr}"
        if output.returncode != 0:
            formated = f"{formated}\nProcess exited with code {output.returncode}"
        if formated == "STDOUT: b''\nSTDERR: b''":
            return "No output produced"
        return formated
    except Exception as error:
        return f"Error: executing Python file: {error}"