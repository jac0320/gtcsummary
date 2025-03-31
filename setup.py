import nltk
import os

def download_nltk_data():
    """Download required NLTK data packages."""
    # Create a directory for NLTK data in the current directory
    nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')
    os.makedirs(nltk_data_dir, exist_ok=True)
    
    # Set NLTK data path to our custom directory
    nltk.data.path.append(nltk_data_dir)
    
    # Download required packages
    required_packages = ['punkt', 'stopwords']
    for package in required_packages:
        try:
            nltk.download(package, download_dir=nltk_data_dir)
        except Exception as e:
            print(f"Error downloading {package}: {e}")

if __name__ == "__main__":
    download_nltk_data() 