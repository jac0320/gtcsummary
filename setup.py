import nltk
import os

def setup_directories():
    """Set up required directories and download NLTK data."""
    # Create directories
    directories = {
        'nltk_data': os.path.join(os.getcwd(), 'nltk_data'),
        'llama_index_cache': os.path.join(os.getcwd(), 'llama_index_cache')
    }
    
    for dir_name, dir_path in directories.items():
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")
    
    # Set environment variable for llama-index cache
    os.environ['LLAMA_INDEX_CACHE_DIR'] = directories['llama_index_cache']
    
    # Configure NLTK data path
    nltk.data.path.append(directories['nltk_data'])
    
    # Download required packages
    required_packages = ['punkt', 'stopwords']
    for package in required_packages:
        try:
            nltk.download(package, download_dir=directories['nltk_data'], quiet=True)
            print(f"Downloaded NLTK package: {package}")
        except Exception as e:
            print(f"Error downloading {package}: {e}")

if __name__ == "__main__":
    setup_directories() 