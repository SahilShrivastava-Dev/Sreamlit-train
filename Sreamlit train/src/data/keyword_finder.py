from src.helper.modules_packages import (
    os,
    PdfReader
)
# import os
# from PyPDF2 import PdfReader

def search_keyword_in_pdf(pdf_file_path, keyword):
    occurrences = 0

    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PdfReader(file)

        for page_num in range(len(pdf_reader.pages)):
            text = pdf_reader.pages[page_num].extract_text().lower()  # Convert to lowercase for case-insensitive search

            if keyword.lower() in text:
                occurrences += 1

    return occurrences

def search_keyword_in_directory(directory_path, keyword):
    sum=0
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory_path, filename)
            occurrences = search_keyword_in_pdf(file_path, keyword)
            
            if occurrences > 0:
                sum+=1
                print(f'Word found in file {filename}, number of occurrences: {occurrences}')
    print(sum)            

# Replace 'your_directory_path' with the actual path to your PDF files directory
directory_path = 'C:/Users/sahil/OneDrive/Desktop/Sreamlit train/Sreamlit train/data/pdf'
keyword_to_search = 'copra'

search_keyword_in_directory(directory_path, keyword_to_search)
