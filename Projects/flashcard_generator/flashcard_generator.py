import pdfplumber
import nltk
import pandas as pd
import re

nltk.download("punkt")
nltk.download('punkt_tab') 
"""
    Downloads the Punkt tokenizer:
    - Punkt is a pre-trained sentence tokenizer used by NLTK
    - It helps split text into sentences
"""

# Function to extract text from PDF
def extract_text_from_PDF(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for pages in pdf.pages:
            text += pages.extract_text() + "\n"
        return text
'''
This function takes a PDF file path -> opens it with pdfplumber ->
goes through each page -> extracts text -> combines all into one big string -> 
returns that text.
'''

# Function to pre-process text
def preprocess_text(text):
    text = re.sub(r'\s+',' ',text)
    text = re.sub(r'\d+',' ',text)
    return text.strip()
'''
This function takes text -> removes extra spaces/newlines -> removes numbers ->
trims unwanted spaces -> returns clean text
'''

# Function to create simple flashcards
def create_flashcard(text):
    sentences = nltk.sent_tokenize(text)
    flashcards = []

    for sentence in sentences:
        if " is " in sentence:  
            parts = sentence.split(" is ")
            if len(parts) == 2:                           #If sentence looks like "X is Y"
                question = f"What is {parts[0].strip()}?" #Create question:"What is X?"
                answer = parts[1].strip()                 #Answer:"Y"
                flashcards.append([question, answer])     #Save as a flashcard (Q&A pair)
        elif " are " in sentence: 
            parts = sentence.split(" are ")
            if len(parts) == 2:                           #If sentence looks like "X are Y"
                question = f"What are {parts[0].strip()}?"#Create question:"What are X?"
                answer = parts[1].strip()                 #Answer:"Y"  
                flashcards.append([question, answer])     #Save as a flashcard (Q&A pair)

    return flashcards
'''
This function scans text → splits it into sentences → finds "X is Y" or "X are Y" sentences → converts them into Q&A flashcards → returns them in a list.
''' 

if __name__ == "__main__":
    pdf_path = "sample.pdf"
    text = extract_text_from_PDF(pdf_path)
    clean_text = preprocess_text(text)

    flashcards = create_flashcard(clean_text)

    df = pd.DataFrame(flashcards, columns=["Question","Answer"])
    df.to_csv("flashcards.csv", index=False)

    print("Flashcards generated and saved as flashcards.csv")
'''
This block is the main workflow: PDF -> Text -> Clean -> Flashcards -> Save CSV ->
Print Done.
'''