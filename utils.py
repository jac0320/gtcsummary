import os
import time

def collect_md_files(folder_path):
    """
    Recursively collects all .md files from a specified folder.

    Parameters:
    - folder_path (str): The path to the folder from which to collect .md files.

    Returns:
    - list[str]: A list of full paths to the .md files found within the folder and its subfolders.
    """
    md_files = []

    # Walk through the directory
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                md_files.append(full_path)

    return md_files


def stream_data(response):
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.02)