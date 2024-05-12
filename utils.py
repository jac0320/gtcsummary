import os
import re
import time
import numpy as np


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


def extract_code_segments(response) -> str:
    """
    Extracts code segments from a given response using regex ```python ... ```.
    """

    pattern = r"```python(.*?)```"
    matches = re.search(pattern, response, re.DOTALL)
    if matches:
        return matches.group(1)


def postprocess_strings(response, as_type=str):
    
    """
    Post-processes the response string to remove unwanted characters.
    """
    return response.strip()


def find_most_similar_index(a, embedding_list):
    a_normalized = a / np.linalg.norm(a)
    embedding_list_normalized = np.array(embedding_list) / np.linalg.norm(embedding_list, axis=1)[:, np.newaxis]
    similarities = np.dot(embedding_list_normalized, a_normalized)
    most_similar_index = np.argmax(similarities)
    return most_similar_index