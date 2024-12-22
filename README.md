# PDF to Image Converter

This project provides Python scripts for converting PDFs to images using the `pdf2image` library. The project is set up to handle both single PDF files and batch processing of multiple PDFs in a folder. 
---

## Prerequisites

### 1. Download and Install Poppler for Windows
- Poppler is required to convert PDFs to images.
- Download it from the official repository: [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/)
- Extract the downloaded archive to a folder,

### 2. Install Python and Pip
Ensure you have Python installed on your system. If `pip` is not installed, you can install it by running:
```bash
python -m ensurepip --upgrade
```

Then, install the required libraries:
```bash
pip install pdf2image python-dotenv
```

---

## Project Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory of the project and configure the following variables:
```dotenv
# Path to the Poppler binary
POPLER_PATH=

# Path to the PDF file(for single file)
PDF_PATH=

# Folder to save the converted images
SAVING_FOLDER=

# Path to the source folder with PDF files
SOURCE_FOLDER=

### 3. Folder Structure
Your project should have the following structure:
```
project-folder/
|-- .env
|-- .gitignore
|-- multiplefiles.py
|-- singlefile.py
|-- saving/ (created automatically if it doesn't exist)

```

---

## Usage

### Single File Conversion
Use `singlefile.py` to convert a single PDF file to images:
```bash
python singlefile.py
```

### Batch Processing
Use `multiplefiles.py` to process all PDF files in the `SOURCE_FOLDER`:
```bash
python multiplefiles.py
```

---

## Notes
- The `.env` file is used to store paths for Poppler, source PDFs, and saving the output images. Make sure this file is configured correctly before running the scripts.
- You do not need to add Poppler to the system's PATH; simply provide its location in the `.env` file under the `POPLER_PATH` variable.
- Ensure that the `saving` folder exists, or the script will create it automatically.
