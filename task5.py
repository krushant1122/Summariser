import PyPDF2
from summarizer import Summarizer

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file_path):
    text = ""
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function to summarize text to a specified word count
def summarize_text(text, word_count=500):
    summarizer = Summarizer()
    summary = summarizer(text, min_length=word_count)
    return summary

# Path to the PDF file you want to summarize
pdf_file_path = 'Operations Management.pdf'

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_file_path)

# Summarize the text to 500 words
summary = summarize_text(pdf_text, word_count=500)

# Save the summary to a text file
with open('summary.txt', 'w') as file:
    file.write(summary)

print("Summary saved to 'summary.txt'")
