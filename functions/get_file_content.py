import os

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
            if len(file_content_string) == 10000:
                file_content_string += f' [...File "{file_path}" truncated at 10000 characters]'
        f.close()
        return file_content_string
    except Exception as error:
        return f"Error:{error}"