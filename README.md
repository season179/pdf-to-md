# PDF to Markdown Converter

## Overview
This Python script converts PDF files to Markdown format using PyMuPDF4LLM, which provides excellent text structure preservation and formatting.

## Features
- Simple and efficient PDF to Markdown conversion
- Preserves document structure and formatting
- Supports selective page conversion
- Compatible with PyMuPDF Pro for Office document support

## Prerequisites
- Python 3.7+
- pip (Python package manager)

## Installation
1. Clone this repository
2. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
```bash
python pdf_to_markdown.py input.pdf [-o output.md]
```

### Arguments
- `input.pdf`: Path to the input PDF file (required)
- `-o, --output`: Path to the output Markdown file (optional, defaults to input filename with .md extension)

## Advanced Usage
The script can be imported and used in other Python projects:

```python
from pdf_to_markdown import convert_pdf_to_markdown

# Convert PDF to Markdown
convert_pdf_to_markdown("input.pdf", "output.md")
```

## Office Document Support
To enable Office document support, install PyMuPDF Pro and use it as follows:

```python
import pymupdf4llm
import pymupdf.pro
pymupdf.pro.unlock()
md_text = pymupdf4llm.to_markdown("sample.doc")
```

## Contributing
Feel free to open issues or submit pull requests to improve the script.