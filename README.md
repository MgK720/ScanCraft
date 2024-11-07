# ScanCraft - Document Scanner and Text Extraction App 
**Work in Progress - This application is currently under development. Some features may be incomplete or subject to change.**

ScanCraft is a desktop application for scanning physical documents, extracting text from them, and exporting the data into a structured JSON format. The application allows users to define custom templates for specifying areas on scanned documents that should be processed and converted into text. It is designed to work with scanners using the TWAIN protocol, process the scanned images, and extract relevant data using Optical Character Recognition (OCR).

## Features
- Scan multiple documents using TWAIN-compatible scanners.
- Define custom templates to select regions on the scanned document for text extraction.
- Extract text using **OCR** (Optical Character Recognition) from selected regions.
- Export extracted data into **JSON** format.
- Future improvements could include AI-based text extraction with TensorFlow or PyTorch to improve recognition accuracy on skewed or poorly scanned documents.

## Technologies and Frameworks

This application is built using the following technologies:

- **Python**: A powerful and flexible language for rapid development of cross-platform applications.
- **PyQt5**: A set of Python bindings for Qt, used to create a user-friendly and responsive graphical interface for the application.
- **PyTwain**: A Python wrapper for TWAIN, allowing interaction with scanners to acquire scanned images.
- **Pytesseract**: A Python wrapper for **Tesseract OCR**, which will be used to extract text from images.
- **OpenCV**: A library for computer vision tasks, used for image manipulation (e.g., deskewing and cropping the scanned documents).
- **Pillow**: A Python Imaging Library (PIL) fork, used for general image processing tasks, such as image manipulation and format conversion.
- **JSON**: The native Python library for working with JSON, used to store and export the extracted text in a structured format.

### Optional future improvements:
- **TensorFlow** or **PyTorch**: For implementing AI-based models that can improve text extraction accuracy, especially for distorted or rotated documents.

## Installation

To set up and run the application, follow the steps below:

### 1. Clone the repository
```bash
git clone https://github.com/mgk720/scancraft.git
cd scancraft
```
### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```
### 3. Install the required dependencies
```bash
pip install -r requirements.txt
```
### 4. Install additional system dependencies (if applicable)
- **Windows**: You'll need to install the TWAIN driver for your scanner.
- **Tesseract OCR**: You also need to install Tesseract OCR separately.
	- **Windows**: Download the installer from Tesseract OCR GitHub and follow the installation instructions.
	- After installation, add Tesseract to your system's PATH.
```bash
pip install pytesseract
```
### 5. Run the application
To start the application, simply run the following command:
```bash
python main.py
```
### Future Plans: Installer for Easy Setup

In the future, I plan to release an **installer** to simplify the setup process. This installer will handle the installation of dependencies, set up necessary configurations, and provide a more user-friendly experience for running the application. Here are the tools and frameworks I will use for the installer:

- **PyInstaller**: I will use this tool to bundle the Python application into a single executable file (e.g., `.exe` for Windows). This ensures that all dependencies are included and that users do not need to manually install Python or any required libraries.

- **Inno Setup**: After creating the executable with PyInstaller, I will use Inno Setup to generate a Windows installer package. Inno Setup is lightweight and easy to use, and it will allow me to create a professional installer that guides users through the installation process, including setting up files and creating shortcuts.

- **NSIS (Nullsoft Scriptable Install System)**: As an alternative to Inno Setup, I might consider using NSIS to create custom installation scripts. It offers more flexibility and can be used to handle more complex installation scenarios if needed.

- **For macOS**: I will use **py2app** to create a macOS `.app` bundle. This will allow users to install the app by simply dragging it into the Applications folder, which is the standard way of distributing macOS apps.

- **For Linux**: For Linux systems, I plan to provide an **AppImage** or **Snap** package. These formats are portable and work across various Linux distributions without the need for installation, making it easier for Linux users to run the application.

By using these tools, I aim to provide a seamless and straightforward installation process, allowing users to install and run the application on their system with minimal effort and without the need for technical knowledge.

## The workflow of the application is as follows:

### Step 1: **Create a Template**
1. Click the **"Create Template"** button to start the template creation process.
2. The application will wait for you to scan a document.
3. Once the document is scanned, the scanned image will be displayed in a preview window.
4. Use the mouse to draw **rectangular areas** on the document, marking the sections you want to extract text from. These areas will be stored in the template.
5. Once you're satisfied with the template, click **"Save Template"**.
6. You will be prompted to **name the template** for future use.

### Step 2: **Scan Documents Using a Template**
1. After creating and saving your template, click the **"Scan"** button.
2. A window will appear displaying all **available templates** that you have created.
3. Select the template that you want to use for the current scan.
4. The scanner will start scanning the documents. If you're using an automatic document feeder (ADF) with your scanner, it will scan multiple pages one after another.
5. As each page is scanned, the application will display a preview of the page, automatically extracting text from the defined areas in the selected template.
6. The application will repeat this process for all pages scanned, displaying each page in sequence.
7. Once all pages have been scanned, click the **"Done"** button.

### Step 3: **Save the Data**
1. After clicking **"Done"**, the application will generate a **JSON** file containing all extracted data.
2. The filename of the JSON file will be based on the selected template and the scan session. For example, if your template is named "Invoice Template", the generated file might be named `InvoiceTemplate_001.json`, where `001` is the ID of the scanning session.
3. The **JSON file** will store the extracted data in a structured format, which you can use for further processing or analysis.

### Example Output (JSON format)
```json
[
    {
        "document_id": "12345",
        "extracted_data": {
            "name": "John Doe",
            "address": "1234 Elm Street",
            "date": "2024-11-07"
        }
    },
    {
        "document_id": "12346",
        "extracted_data": {
            "name": "Jane Smith",
            "address": "5678 Oak Avenue",
            "date": "2024-11-08"
        }
    }
]
```
## Project Structure
```bash
scancraft/
├── main.py            # Main application file
├── scanner.py         # Handles interaction with the scanner (PyTwain)
├── template.py        # Logic for defining and saving templates
├── extract_text.py    # Text extraction logic using Pytesseract
├── requirements.txt   # List of required Python dependencies
├── README.md          # This file
└── assets/            # Folder for images and icons
```

## Future Improvements
- **AI-based text extraction**: Using machine learning frameworks like TensorFlow or PyTorch, the application could intelligently detect and correct for document distortions, skewed scans, and varied text positioning.
- **Multi-language support**: Expand the OCR capabilities to support more languages by integrating more Tesseract language models.
- **Improved error handling**: More robust error handling for issues with scanners, images, or OCR errors.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Contributing
Contributions to the project are welcome! If you want to add new features, fix bugs, or improve documentation, feel free to open a pull request. Please follow the standard GitHub contribution workflow.
