import requests
import pdfplumber
import pytesseract
from pdf2image import convert_from_path
import os
import shutil
#hello
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
            print("PDF received")
        else:
            print(f"Failed to download PDF. Status code: {response.status_code}, Content-Type: {response.headers.get('Content-Type')}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to extract text from PDF using OCR
def extract_text_ocr(pdf_path):
    text = ""
    try:
        # Convert PDF to images
        pages = convert_from_path(pdf_path)
        
        # Iterate through all the pages stored above
        for i, page in enumerate(pages):
            # Save the image of the page in system
            print("Now Processing Page", i+1,)
            image_path = f'page_{i}.jpg'
            page.save(image_path, 'JPEG')
            
            # Use Tesseract to do OCR on the image
            text += pytesseract.image_to_string(image_path)
            
            # Remove the image file after processing
            os.remove(image_path)
        
    except Exception as e:
        print(f"An error occurred while extracting data: {e}")
    return text

# Download PDF from URL and extract text using OCR
pdf_url = 'https://canadabuys.canada.ca/sites/default/files/webform/tender_notice/40540/202403795---rfp-%28final.pdf'
pdf_url = 'https://canadabuys.canada.ca/sites/default/files/webform/tender_notice/40211/1000033838c_rfb_eng.pdf'
""" pdf_url = 'https://canadabuys.canada.ca/sites/default/files/webform/tender_notice/39850/202400584---rfb-%28psib_en.pdf'
pdf_url = 'https://canadabuys.canada.ca/sites/default/files/webform/tender_notice/34472/en_rfp_j074110.pdf'
pdf_url = "https://canadabuys.canada.ca/sites/default/files/webform/tender_notice/7467/rfp---english.pdf" """

pdf_path = 'downloaded_file2.pdf'

download_pdf(pdf_url, pdf_path)
text = extract_text_ocr(pdf_path)

# Store text in .txt file
with open("downloaded_file2_ocr.txt", "w") as f:
    f.write(text)


#separate text into lines to more easily manipulate
text_list = text.splitlines()
oldlen=len(text_list)

#open a new file to store altered text
f = open("test2.txt", "w")
#Loop through lines of text and make changes
filtered_text=[]
j=0
for i in text_list:
    if ("" not in i) and ("" not in i) and ("☐" not in i) and ("Table - A" not in i) and ("Table : A" not in i) and ("Table A" not in i) and ("TABLE - A" not in i) and ("TABLE : A" not in i) and ("TABLE A" not in i):
        if "Quantity Required" in i:
            for k in range(1,6):
                if text_list[j+k].isnumeric() or ("@" in text_list[j+k]):
                    value=text_list[j+k]
                    value = value.replace("@ ", "")
            
            filtered_text.append(i)
            filtered_text.append(value)

        if "Solicitation closes" in i:
            filtered_text.append("Solicitation closes:")
            for l in range(1,8):
                if "on" in text_list[j+l] or "at" in text_list[j+l]:
                    filtered_text.append(text_list[j+l])

    else:
        filtered_text.append(i)
    j+=1
    
#write lines that we will be keeping for alterations to file
for i in filtered_text:
    f.write(i)
    f.write("\n")
f.close()
