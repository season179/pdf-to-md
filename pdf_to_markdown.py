import os
import argparse
import pymupdf4llm
from pathlib import Path

def convert_pdf_to_markdown(pdf_path, output_path=None):
    """
    Convert PDF to Markdown using PyMuPDF4LLM.
    
    Args:
        pdf_path (str): Path to the input PDF file
        output_path (str, optional): Path to save the output Markdown file
    """
    try:
        # Convert PDF to Markdown
        md_text = pymupdf4llm.to_markdown(pdf_path)
        
        # If no output path specified, create one based on input filename
        if not output_path:
            output_path = str(Path(pdf_path).with_suffix('.md'))
            
        # Save the Markdown file
        Path(output_path).write_bytes(md_text.encode())
        print(f"Markdown file saved to {output_path}")
        
    except Exception as e:
        print(f"Error converting PDF: {e}")

def main():
    parser = argparse.ArgumentParser(description='Convert PDF to Markdown using PyMuPDF4LLM')
    parser.add_argument('input', help='Input PDF file path')
    parser.add_argument('-o', '--output', help='Output Markdown file path')
    
    args = parser.parse_args()
    convert_pdf_to_markdown(args.input, args.output)

if __name__ == '__main__':
    main()