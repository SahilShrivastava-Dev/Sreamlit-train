import streamlit as st
import numpy as np
import plotly.graph_objects as go
# from llama_index.embeddings import AzureOpenAIEmbedding
# from llama_index.llms import AzureOpenAI
import os

# OPENAI_KEY = os.getenv('OPENAI_API_KEY')
# ENDPOINT = os.getenv('OPENAI_API_BASE')
# OPENAI_VERSION = os.getenv('OPENAI_API_VERSION')


# def select_llm():
#     return AzureOpenAI(
#     model='gpt-35-turbo',
#     deployment_name='bot-llm',
#     api_key=OPENAI_KEY,
#     azure_endpoint=ENDPOINT,
#     api_version=OPENAI_VERSION
#     )

# def select_embedding():
#     return AzureOpenAIEmbedding(
#     model='text-embedding-ada-002',
#     deployment_name='bot-embedding',
#     api_key=OPENAI_KEY,
#     azure_endpoint=ENDPOINT,
#     api_version=OPENAI_VERSION
#     )


def fetch_data_from_azure(option1, option2, option3, option4_date, option5_date):
    # Here you will make API call to Azure OpenAI to fetch data based on selected options
    # Replace this function with actual API call
    # For demonstration purposes, I'm returning random data
    
    # Sample data
    labels = ['A', 'B', 'C', 'D']
    values = [20, 30, 40, 10]
    
    return labels, values

def main():
    st.set_page_config(page_title="Sentiment Analysis", page_icon=":tada:", layout="wide")
    # Title and search bar
    st.title("Fixed Sidebar Example")
    search_query = st.text_input("Search:", "")

    # Fixed sidebar with reduced width
    st.sidebar.title("Sentiment Analysis Filters")
    st.sidebar.markdown("---")
    sidebar_width = 200
    st.markdown(f'<style>div[role="listbox"] .selectbox-container {{ width: {sidebar_width}px; }}</style>', unsafe_allow_html=True)
    
    # Dropdown menus on the left side
    option1 = st.sidebar.selectbox("Products", ["Copra", "Crude palm oil", "Crude sunflower oil", "Herbs", "Botanical extracts", "Coconut oil", "Olive oil", "Castor oil", "Glycerin", "Lanolin", "Sodium laureth sulfate", "Fragrance compounds", "Parabens", "Vitamin E", "Vitamin C", "Wheat flour", "Spices", "Lentils", "Rice", "Oats"]
, key="option1")
    search_query = f"{option1} news"
    st.write(f"Displaying news for {option1}")

    # Get the absolute path of the web2pdf.ipynb file
    web2pdf_path = os.path.join(os.path.dirname(__file__), 'C:/Users/sahil/OneDrive/Desktop/Sreamlit train/Sreamlit train/src/data', 'web2pdf.ipynb')

    # Run the web2pdf.ipynb file
    os.system(f'jupyter nbconvert --execute {C:/Users/sahil/OneDrive/Desktop/Sreamlit train/Sreamlit train/src/data/web2pdf.ipynb}')

    option2 = st.sidebar.selectbox("Geographical Location ", ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
, key="option2")
    option3 = st.sidebar.selectbox("Sentiment Type", ["Financial Sentiment", "Regional Sentiment", "Environmental Sentiment", "Social Sentiment", "Ethical Sentiment", "Quality Sentiment", "Health and Safety Sentiment", "Innovation Sentiment", "Cultural Sentiment", "Market Sentiment"]
, key="option3")

    # Calendar widget for option 4
    option4_date = st.sidebar.date_input("Date from which sentiments is required", key="option4_date")

    # Calendar widget for option 5
    option5_date = st.sidebar.date_input("Date until which sentiment is required", key="option5_date")
    
    option6 = st.sidebar.selectbox("Option 6", ["Option 6-A", "Option 6-B", "Option 6-C"], key="option6")
    
    # Search button
    search_button = st.sidebar.button("Search")

    # Display selected options
    st.write("---")
    st.write("Selected options:")
    st.write("Products:", option1)
    st.write("Geographical Location:", option2)
    st.write("Sentiment Type:", option3)
    st.write("Date From:", option4_date)
    st.write("Date From:", option5_date)
    st.write("Option 6:", option6)
    
    # Fetch data from Azure OpenAI
    labels, values = fetch_data_from_azure(option1, option2, option3, option4_date, option5_date)
    
    # Right side - plot based on select box
    st.write("---")
    st.title("Plot Options")
    plot_type = st.selectbox("Select Plot Type", ["Pie Chart", "Bar Plot", "Line Chart", "Scatter Plot"], key="plot_type")

    # Render plot based on selection
    if plot_type == "Pie Chart":
        render_pie_chart(labels, values)
    elif plot_type == "Bar Plot":
        render_bar_plot(labels, values)
    elif plot_type == "Line Chart":
        render_line_chart(labels, values)
    elif plot_type == "Scatter Plot":
        render_scatter_plot(labels, values)

def render_pie_chart(labels, values):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    st.plotly_chart(fig)

def render_bar_plot(labels, values):
    fig = go.Figure(data=[go.Bar(x=labels, y=values)])
    st.plotly_chart(fig)

def render_line_chart(labels, values):
    fig = go.Figure(data=[go.Scatter(x=labels, y=values)])
    st.plotly_chart(fig)

def render_scatter_plot(labels, values):
    fig = go.Figure(data=[go.Scatter(x=labels, y=values, mode='markers')])
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
