import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF 
from gnews import GNews
import urllib3
from reportlab.pdfgen import canvas
import aspose.pdf as ap



google_news = GNews()
search_query = 'Copra '  # Replace 'Your Product' with the product you want to search for
product_news = google_news.get_news(search_query)

print(product_news) 

# Converting JSON data into DataFrame
df = pd.DataFrame(product_news)
print(df)
url = "https://news.google.com/rss/articles/CBMiL2h0dHBzOi8vd3d3LmZpaml0aW1lcy5jb20uZmovY29wcmEtdHJhZGUtZHlpbmcv0gEA?oc=5&hl=en-IN&gl=IN&ceid=IN:en"
res = requests.get(url, verify=False)
html_page = res.content

        # Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html_page, 'html.parser')
text_content = soup.get_text()
html_page
text_content
import os
import requests
from bs4 import BeautifulSoup
import aspose.pdf as ap

def save_pdf(url, counter):
    try:
        res = requests.get(url, verify=False)
        res.raise_for_status()

        html_page = res.content

        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(html_page, 'html.parser')
        text_content = soup.get_text()

        print(type(text_content))

        # Specify the full path for saving the PDF
        output_path = os.path.join("C:/Users/sahil/OneDrive/Desktop/Sreamlit train/Sreamlit train/data/pdf", f"output{counter}.pdf")

        # Initialize document object
        document = ap.Document()

        # Add page
        page = document.pages.add()

        # Initialize textfragment object
        text_fragment = ap.text.TextFragment(text_content)

        # Add text fragment to new page
        page.paragraphs.add(text_fragment)

        # Save updated PDF to the specified location
        document.save(output_path)
        print('saved',counter)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Assuming df is a DataFrame with a column named 'url'
# Iterate through each URL and apply the function with a counter
for i, url in enumerate(df['url'], start=1):
    save_pdf(url, i)
