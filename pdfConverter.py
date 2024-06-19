import requests
import pdfplumber

def download_pdf(pdf_url, output_path):
    #gets pdf content and stores it in a local file to be converted to text later

    try:
        #immitates browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
        }
        response = requests.get(pdf_url, headers=headers, allow_redirects=True)

        # Check if the request was successful
        if response.status_code == 200 and response.headers['Content-Type'] == 'application/pdf':
            # Open a local file with write-binary mode
            with open(output_path, 'wb') as file:
                # Write the content of the response (which is the PDF) to the local file
                file.write(response.content)
            print("PDF received")
        else:
            print(f"Failed to download PDF. Status code: {response.status_code}, Content-Type: {response.headers.get('Content-Type')}")
    except Exception as e:
        print(f"An error occurred: {e}")

def extract_text_and_tables(pdf_path):
    #extracts text and tables from pdf, stores in tables_text and text variables, and prints them

    text = ""
    tables_text = ""
    try:
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
    except Exception as e:
        print(f"An error occurred while extracting data: {e}")
    return text, tables_text




# Example usage
pdf_url = 'https://canadabuys.canada.ca/sites/default/files/webform/tender_notice/31198/request-for-proposal-%28rfp---office-seating-sa---english-pers-svcs.pdf'
pdf_path = 'downloaded_file.pdf'

download_pdf(pdf_url, pdf_path)
text, tables_text = extract_text_and_tables(pdf_path)

print("Extracted Text:")
print(text)

print("Extracted Tables:")
print(tables_text)