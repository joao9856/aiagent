import os

def get_files_info(working_directory, directory=None):
    try:
        wkd = os.path.abspath(working_directory)
        dir = os.path.abspath(os.path.join(working_directory, directory))
        if dir.startswith(wkd) == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if os.path.isdir(dir) == False:
            return f'Error: "{directory}" is not a directory'
        string = ""
        for item in os.listdir(dir):
            dest = os.path.abspath(os.path.join(dir, item))
            string += f"- {item}: filesize={os.path.getsize(dest)} bytes, is_dir={os.path.isdir(dest)}\n"
        return string.rstrip("\n")
    except Exception as error:
        return f"Error:{error}"