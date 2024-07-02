import requests
import pdfplumber
import pytesseract
from pdf2image import convert_from_path
import os
import shutil

# Function to download PDF
def download_pdf(pdf_url, output_path):
    try:
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
        if response.status_code == 200 and response.headers['Content-Type'] == 'application/pdf':
            with open(output_path, 'wb') as file:
                file.write(response.content)
            print("PDF downloaded successfully.")
        else:
            print(f"Failed to download PDF. Status code: {response.status_code}, Content-Type: {response.headers.get('Content-Type')}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to extract text from PDF using OCR
def extract_text_ocr(pdf_path):
    text = ""
    try:
        # Convert PDF to images with high resolution
        pages = convert_from_path(pdf_path, 300)
        
        # Iterate through all the pages stored above
        for i, page in enumerate(pages):
            print(f"Processing page {i+1}")
            image_path = f'page_{i}.jpg'
            page.save(image_path, 'JPEG')
            
            # Use Tesseract to do OCR on the image
            text += pytesseract.image_to_string(image_path)
            
            # Remove the image file after processing
            os.remove(image_path)
        
    except Exception as e:
        print(f"An error occurred while extracting text: {e}")
    return text

def extract_text(pdf_path):
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
                        row = [str(cell) if cell is not None else "" for cell in row]
                        tables_text += "\t".join(row) + "\n"
                    tables_text += "\n"
    except Exception as e:
        print(f"An error occurred while extracting data: {e}")
    return text

# Download PDF from url and extract text into text variable
pdf_url = "https://canadabuys.canada.ca/sites/default/files/webform/tender_notice/7467/rfp---english.pdf"
pdf_path = 'downloaded_file2.pdf'

download_pdf(pdf_url, pdf_path)
text = extract_text(pdf_path)

#store text in .txt file
f = open("downloaded_file2.txt", "w")
f.write(text)
f.close()

#separate text into lines to more easily manipulate
text_list = text.splitlines()
oldlen=len(text_list)

#open a new file to store altered text
f = open("test2.txt", "w")
#Loop through lines of text and make changes
filtered_text=[]
j=0
in_table = False
#loop through lines
for i in text_list:
#check if key characters are in text to keep
    #check if we are in table to enable not_kept tracking to prevent missing important lines
    if "Headrest" in i:
        in_table = True
        not_kept = 0
    if "Upholstery" in i: 
        in_table =False

    if ("" not in i) and ("" not in i) and ("☐" not in i) and ("Table - A" not in i) and ("Table : A" not in i) and ("Table A" not in i) and ("TABLE - A" not in i) and ("TABLE : A" not in i) and ("TABLE A" not in i):
        #if not check for quantity required
        if "Quantity Required" in i or ("QTY" in i):
            entry=i.replace("_", "")
            for k in range(1,4):
                if "_" in text_list[j+k]:
                    value=text_list[j+k]
                    value=value.replace("_","")
                    entry=entry+value
            
            filtered_text.append(entry)
            not_kept = 0 #because we did not discard keep as zero/set to zero
        elif "Solicitation closes" in i or "Solicitation Closes" in i:
            filtered_text.append("Solicitation closes:")
            for l in range(1,9):
                if "on –" in text_list[j+l] or "at –" in text_list[j+l]:
                    filtered_text.append(text_list[j+l])
            not_kept = 0 #again because we kept set to 0

        elif in_table and not_kept <3:
            not_kept+=1
            filtered_text.append(i)
        else:
            #dont keep if not in table or if not_kept is too high
            #instead we set to zero and discard
            not_kept = 0

    else:
        filtered_text.append(i)
    j+=1
    
for i in filtered_text:
    f.write(i)
    f.write("\n")
f.close()

shutil.copyfile("test2.txt", "test2final.txt")

#read
f = open("test2final.txt", "r")
data = f.read()
f.close()
box_replace = {
    "": "Y",
    "": "Y",
    "": "Y",
    "": "Y",
    "": "N",
    "☐": "N",
    "": "-",
    "": "->",
    "": ""
}

for i, j in box_replace.items():
    data = data.replace(i,j)

f = open("test2final.txt", "w")
f.write(data)

print(oldlen)
print(len(filtered_text))


