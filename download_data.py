import os
import zipfile
import urllib.request
import shutil
import glob

def download_and_extract_data():
    # Define directories
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    extract_dir = os.path.join(data_dir, "extracted")
    
    # Create directories if they don't exist
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(extract_dir, exist_ok=True)
    
    # Official World Bank API URL for Total Population CSV ZIP
    url = "https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv"
    zip_path = os.path.join(data_dir, "population_dataset.zip")
    
    print(f"Downloading World Bank population dataset from: {url}")
    try:
        # Download the zip file
        urllib.request.urlretrieve(url, zip_path)
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error downloading data: {e}")
        return False
        
    print("Extracting files...")
    try:
        # Extract the ZIP archive
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        print("Extraction completed!")
    except Exception as e:
        print(f"Error extracting ZIP: {e}")
        return False
        
    # Locate files in the extracted directory
    extracted_files = os.listdir(extract_dir)
    print(f"Extracted files: {extracted_files}")
    
    pop_file_pattern = os.path.join(extract_dir, "API_SP.POP.TOTL_DS2_en_csv_v2_*.csv")
    meta_file_pattern = os.path.join(extract_dir, "Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_*.csv")
    
    pop_files = glob.glob(pop_file_pattern)
    meta_files = glob.glob(meta_file_pattern)
    
    if not pop_files or not meta_files:
        print("Error: Could not find the expected population or metadata CSV files.")
        return False
        
    # Rename and move files to the main data/ directory
    final_pop_path = os.path.join(data_dir, "population.csv")
    final_meta_path = os.path.join(data_dir, "metadata.csv")
    
    shutil.move(pop_files[0], final_pop_path)
    shutil.move(meta_files[0], final_meta_path)
    
    print(f"Saved population data to: {final_pop_path}")
    print(f"Saved metadata to: {final_meta_path}")
    
    # Clean up temporary folders and files
    try:
        shutil.rmtree(extract_dir)
        os.remove(zip_path)
        print("Cleaned up temporary download files.")
    except Exception as e:
        print(f"Warning: Cleanup failed: {e}")
        
    print("\nData Science Dataset successfully initialized!")
    return True

if __name__ == "__main__":
    download_and_extract_data()
