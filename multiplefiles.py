import os
from dotenv import load_dotenv
from pdf2image import convert_from_path

# Load environment variables from the .env file
load_dotenv()

# Define paths (after loading the .env file)
poppler_path = os.getenv("POPLER_PATH")
source_folder = os.getenv("SOURCE_FOLDER")
saving_folder = os.getenv("SAVING_FOLDER")

# Ensure directories exist
if not os.path.exists(source_folder):
    raise FileNotFoundError(f"Source folder does not exist: {source_folder}")

if not os.path.exists(saving_folder):
    os.makedirs(saving_folder)  # Create the folder if it doesn't exist

# Loop through all PDF files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(source_folder, filename)
        print(f"Processing: {pdf_path}")

        try:
            # Convert PDF to images
            pages = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
            
            # Save images
            c = 1
            for page in pages:
                img_name = f"{os.path.splitext(filename)[0]}_img-{c}.jpeg"  # Naming based on original PDF file
                page.save(os.path.join(saving_folder, img_name), "JPEG")
                c += 1
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")

print("Conversion complete!")
