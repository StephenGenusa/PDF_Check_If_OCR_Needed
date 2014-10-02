"""
Purpose:
  - Check to see if there is text on any page in a PDF file. If so, leave the 
        PDF filealone. 
    If text is not found, move the file to another directory to be OCR'd
              
Author: Stephen Genusa
   URL: http://development.genusa.com
  Date: September 2014
           
"""

import sys
import os
from PyPDF2 import PdfFileReader


pdf_path = '~/PDFs'
ocr_dir = 'For_OCR'

# Build a list of the PDFs
pdf_files = os.listdir(pdf_path)

files_found = len(pdf_files)
if files_found == 0:
    raise Exception("No files found in the PDF directory. No work to be done.")
print "Found", files_found, "files"

# for each PDF file
for file_no in range(files_found):
    current_filename = pdf_files[file_no]
    # Make sure it's a PDF and not something else
    if current_filename.lower().find('.pdf') > -1:
        print "Checking PDF", current_filename
        found_text = False
        # Load the PDF
        pdf_input =  PdfFileReader(open(os.path.join(pdf_path,current_filename), "rb"))
        # Look through pages for text
        for page in pdf_input.pages:
            page_text = page.extractText()
            if len(page_text) > 0:
                print "Text found in PDF", current_filename
                found_text = True
                break
        # If no text was found, it is a PDF with images and no OCR'd text
        #     so move it to the OCR directory
        if not found_text:
            print "Moving", current_filename
            if not os.path.exists(os.path.join(pdf_path, ocr_dir)):
                os.mkdir(os.path.join(pdf_path, ocr_dir)) 
            os.rename(os.path.join(pdf_path,current_filename), os.path.join(pdf_path, ocr_dir, current_filename))    


print "Done"
