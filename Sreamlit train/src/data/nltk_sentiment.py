# import os
# from nltk.sentiment import SentimentIntensityAnalyzer
# import PyPDF2
# import nltk
# nltk.download('vader_lexicon')


# # Set the path to your PDF files
# pdf_folder_path = r'C:/Users/sahil/OneDrive/Desktop/Sreamlit train/Sreamlit train/data/pdf'


# # Initialize the sentiment analyzer
# sia = SentimentIntensityAnalyzer()

# # Create a dictionary to store the results
# sentiment_results = {}

# # Iterate through each PDF file in the folder
# for filename in os.listdir(pdf_folder_path):
#     if filename.endswith('.pdf'):
#         file_path = os.path.join(pdf_folder_path, filename)

#         # Open the PDF file
#         with open(file_path, 'rb') as file:
#             # Initialize a PDF reader
#             pdf_reader = PyPDF2.PdfReader(file)

#             # Extract text from the PDF
#             text = ''
#             for page_num in range(len(pdf_reader.pages)):
#                 text += pdf_reader.pages[page_num].extract_text()


#             # Perform sentiment analysis
#             sentiment_score = sia.polarity_scores(text)
#             # Determine sentiment label based on compound score
        

#             # Store the result in the dictionary
#             sentiment_results[filename] = sentiment_score
                

# # Print individual sentiment scores
# for filename, score in sentiment_results.items():
#     print(f"{filename}: Sentiment Score - {score}")

# # Print combined sentiment score
# # Calculate combined sentiment score
# # Extract sentiment scores and ensure they are numeric
# sentiment_scores = [score['compound'] for score in sentiment_results.values() if isinstance(score, dict)]

# # Calculate combined sentiment score
# combined_sentiment_score = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0.0
# print(f"\nCombined Sentiment Score for all PDFs: {combined_sentiment_score}")

# # ... (your existing code)

# # Save sentiment_results to a file (pickle format for simplicity)
# import pickle

# with open('sentiment_results.pkl', 'wb') as file:
#     pickle.dump(sentiment_results, file)
#     print("Created",sentiment_results,"lllll")


# You can further use or analyze the 'sentiment_results' dictionary as needed.


# import os
# from nltk.sentiment import SentimentIntensityAnalyzer
# import PyPDF2
# import pickle

# # Set the path to your PDF files
# pdf_folder_path = r'C:\Users\sahil\OneDrive\Desktop\Sreamlit train\Sreamlit train\data\pdf'

# # Initialize the sentiment analyzer
# sia = SentimentIntensityAnalyzer()

# # Create a dictionary to store the results
# # Create a dictionary to store the results
# sentiment_results = {}

# # Iterate through each PDF file in the folder
# for filename in os.listdir(pdf_folder_path):
#     if filename.endswith('.pdf'):
#         file_path = os.path.join(pdf_folder_path, filename)

#         # Open the PDF file
#         with open(file_path, 'rb') as file:
#             # Initialize a PDF reader
#             pdf_reader = PyPDF2.PdfReader(file)

#             # Extract text from the PDF
#             text = ''
#             for page_num in range(len(pdf_reader.pages)):
#                 text += pdf_reader.pages[page_num].extract_text()

#             # Perform sentiment analysis
#             sentiment_score = sia.polarity_scores(text)

#             # Determine sentiment label based on compound score
#             if sentiment_score['compound'] >= 0.05:
#                 label = 'positive'
#             elif sentiment_score['compound'] <= -0.05:
#                 label = 'negative'
#             else:
#                 label = 'neutral'

#             # Store the result in the dictionary with the 'label' key
#             sentiment_results[filename] = {'compound': sentiment_score['compound'], 'label': label}

# # Save sentiment_results to a file (pickle format for simplicity)
# with open('sentiment_results.pkl', 'wb') as file:
#     pickle.dump(sentiment_results, file)


import os
import PyPDF2
import nltk
import pickle
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

# Set the path to your PDF files
pdf_folder_path = r'C:/Users/sahil/OneDrive/Desktop/Sreamlit train/Sreamlit train/data/pdf'
output_path = r'C:/Users/sahil/OneDrive/Desktop/Sreamlit train/Sreamlit train/data/'  # Specify the path where the pkl file should be saved

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Create a dictionary to store the results
sentiment_results = {}

# Iterate through each PDF file in the folder
for filename in os.listdir(pdf_folder_path):
    if filename.endswith('.pdf'):
        file_path = os.path.join(pdf_folder_path, filename)

        # Open the PDF file
        with open(file_path, 'rb') as file:
            # Initialize a PDF reader
            pdf_reader = PyPDF2.PdfReader(file)

            # Extract text from the PDF
            text = ''
            for page_num in range(len(pdf_reader.pages)):
                text += pdf_reader.pages[page_num].extract_text()

            # Perform sentiment analysis
            sentiment_score = sia.polarity_scores(text)
            
            # Determine sentiment label based on compound score
            if sentiment_score['compound'] >= 0.50:
                label = 'positive'
            elif sentiment_score['compound'] <= -0.50:
                label = 'negative'
            else:
                label = 'neutral'

            # Store the result in the dictionary with the 'label' key
            sentiment_results[filename] = {'compound': sentiment_score['compound'], 'label': label}

# Save sentiment_results to a file (pickle format for simplicity)
pkl_file_path = os.path.join(output_path, 'sentiment_results.pkl')
with open(pkl_file_path, 'wb') as file:
    pickle.dump(sentiment_results, file)
    print(f"Sentiment results saved to: {pkl_file_path}")

# Print individual sentiment scores
for filename, score in sentiment_results.items():
    print(f"{filename}: Sentiment Score - {score}")

# Calculate combined sentiment score
sentiment_scores = [score['compound'] for score in sentiment_results.values() if isinstance(score, dict)]
combined_sentiment_score = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0.0
print(f"\nCombined Sentiment Score for all PDFs: {combined_sentiment_score}")
