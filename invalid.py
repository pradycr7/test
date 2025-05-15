# Create a sample invalid PDF content (missing PDF header and EOF marker)
invalid_pdf_content = b"This is not a valid PDF file. It lacks proper PDF structure and markers."

# Write this content to a file for download
invalid_pdf_filename = "invalid_sample.pdf"
with open(invalid_pdf_filename, "wb") as f:
    f.write(invalid_pdf_content)
