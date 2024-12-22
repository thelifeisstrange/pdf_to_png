from pdf2image import convert_from_path
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve environment variables
poppler_path = os.getenv("POPLER_PATH")
pdf_path = os.getenv("PDF_PATH")
saving_folder = os.getenv("SAVING_FOLDER")

# Convert PDF to images
pages = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)

# Save images
c = 1
for page in pages:
    img_name = f"img-{c}.jpeg"
    page.save(os.path.join(saving_folder, img_name), "JPEG")
    c += 1

print("PDF converted to images successfully.")
