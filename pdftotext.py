import pdfplumber

def extract_text_and_tables(pdf_path):
    text = ""
    tables_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Extract text
            if page.extract_text():
                text += page.extract_text() + "\n"
            
            # Extract tables
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    # Replace None with empty string
                    row = [str(cell) if cell is not None else "" for cell in row]
                    tables_text += "\t".join(row) + "\n"
                tables_text += "\n"
    return text, tables_text

# Example usage
pdf_path = "/home/coop/Desktop/example.pdf"
text, tables_text = extract_text_and_tables(pdf_path)
print("Text:\n", text)
print("\nTables:\n", tables_text)