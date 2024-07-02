import requests
import pdfplumber
import re
import shutil

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

def extract_text(pdf_path):
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

# Download PDF from url and extract text into text variable
pdf_url = 'https://canadabuys.canada.ca/sites/default/files/webform/tender_notice/34472/en_rfp_j074110.pdf'
#pdf_url = 'https://canadabuys.canada.ca/sites/default/files/webform/tender_notice/40540/202403795---rfp-%28final.pdf'
pdf_path = 'downloaded_file2.pdf'

download_pdf(pdf_url, pdf_path)
text, tables_text = extract_text(pdf_path)

if tables_text not in text:
    text=text+tables_text



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
for i in text_list:
    if ("" not in i) and ("" not in i) and ("☐" not in i):
        if "Quantity Required" in i:
            entry=i.replace("_", "")

            for k in range(1,4):
                if "_" in text_list[j+k]:
                    value=text_list[j+k]
                    value=value.replace("_","")
                    entry=entry+value
            
            filtered_text.append(entry)


        if "Solicitation closes" in i:
            filtered_text.append("Solicitation closes:")
            for l in range(1,9):
                if "on –" in text_list[j+l] or "at –" in text_list[j+l]:
                    filtered_text.append(text_list[j+l])

    else:
        filtered_text.append(i)
    j+=1
    
#write lines that we will be keeping for alterations to file
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




