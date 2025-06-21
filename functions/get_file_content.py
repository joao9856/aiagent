import os
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        wkd = os.path.abspath(working_directory)
        file = os.path.abspath(os.path.join(working_directory, file_path))
        if file.startswith(wkd) == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(file) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        MAX_CHARS = 10000
        with open(file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == 100000:
                file_content_string += f' [...File "{file_path}" truncated at 10000 characters]'
        f.close()
        return file_content_string
    except Exception as error:
        return f"Error:{error}"

schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Retrieves file from the specified file up to the maximum of 10000 characters, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file to retrieve from, relative to the working directory.",
                ),
            },
        ),
    )