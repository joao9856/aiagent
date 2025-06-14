import os

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