import re
import requests
import os
import PyPDF2
import shutil

def extract_text_from_arxiv_pdf(pdf_path, output_txt_path):
    # Open the PDF file
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        # Extract text from each page
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()

    # Save the extracted text to a file
    with open(output_txt_path, "w") as text_file:
        text_file.write(text)

# Function to download PDF from URL
def download_pdf(url, output_dir):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(output_dir, os.path.basename(url)), 'wb') as f:
                f.write(response.content)
                print(f"Downloaded {url}")
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


def getArchiveLinks(filePath):
    # Open the text file
    with open(filePath, 'r') as file:
        # Initialize an empty list to store the second elements
        research_links = []
        
        # Read each line in the file
        for line in file:
            # Split the line by whitespace
            links = line.strip().split()
            
            # Check if the second element exists and is not "None"
            if len(links) > 1 and links[1] != "None":
                # Add the second element to the list
                research_links.append(links[1])

    # Print the list of second elements
    return research_links

def archiveLinkAbsToPdf(url):
    # Define the regex pattern to match the URL
    pattern = r".+arxiv.org/abs/(\d+\.\d+)"
    # Check if the pattern matches the URL
    match = re.match(pattern, url)
    # If there's a match, perform the substitution
    if match:
        # Perform the substitution by replacing 'abs' with 'pdf'
        new_url = "https://arxiv.org/pdf/" + match.group(1)
        return new_url
    return url

def delete_directory(directory):
    try:
        shutil.rmtree(directory)
    except Exception as e:
        print(f'Failed to delete and recreate {directory}. Reason: {e}')
        
if __name__ == "__main__":
    
    # list = getArchiveLinks("./Links/OpenAI_Research.txt")
    
    # # Output directory to save PDFs
    pdf_dir = "./Articles/OpenAI/pdf"

    # Create output directory if it doesn't exist
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)

    # Download each PDF
    for link in list:
        pdfUrl = archiveLinkAbsToPdf(link)
        download_pdf(pdfUrl, pdf_dir)
    
    text_dir = "./Articles/OpenAI/txt"
    if not os.path.exists(text_dir):
        os.makedirs(text_dir)
        
    # Iterate over all the files in the directory
    for filename in os.listdir(pdf_dir):
        file_path = os.path.join(pdf_dir, filename)
        
        # Check if it is a file
        if os.path.isfile(file_path):
            extract_text_from_arxiv_pdf(file_path, text_dir + "/" + filename + ".txt")

    delete_directory(pdf_dir)    
