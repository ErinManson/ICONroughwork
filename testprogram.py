import requests
import pdfplumber

# URL of the PDF file
pdf_url = 'https://canadabuys.canada.ca/sites/default/files/webform/tender_notice/31198/amendment-005-to-solicitation-w0107.pdf'

# Send a GET request to the URL
response = requests.get(pdf_url)

# Check if the request was successful
if response.status_code == 200:
    # Open a local file with write-binary mode
    with open('downloaded_file.pdf', 'wb') as file:
        # Write the content of the response (which is the PDF) to the local file
        file.write(response.content)
        file.close()
    print("PDF recieved")
else:
    print(f"Failed to download PDF. Status code: {response.status_code}")

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
pdf_path = 'downloaded_file.pdf'
text, tables_text = extract_text_and_tables(pdf_path)
print(text, tables_text)