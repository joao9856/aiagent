import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        wkd = os.path.abspath(working_directory)
        file = os.path.abspath(os.path.join(working_directory, file_path))
        if file.startswith(wkd) == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.exists(file) == False:
            os.makedirs(file.rstrip(file_path))
            #os.fil(file)
        with open(file, "w") as f:
            f.write(content)
        f.close()
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as error:
        return f"Error:{error}"


schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Writes file with the name provided in file_path with the content provided in content, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file to write to, if it doesnt exist it will be automatically be created, relative to the working directory.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The content to be written to the file.",
                ),
            },
        ),
    )