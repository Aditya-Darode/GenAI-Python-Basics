from PyPDF2 import PdfWriter  # Importing PdfWriter to merge PDFs

merger = PdfWriter()  # Creating a PDF merger object
pdfs = []  # List to store PDF file names

# Ask user how many PDFs they want to merge
n = int(input("How many pdfs do you want to merge?\n"))

# Taking PDF names from user and adding to the list
for i in range(0, n):
    name = input(f"Enter the name of pdf {i + 1}: ")
    pdfs.append(name)

# Append each PDF into the merger
for pdf in pdfs:
    merger.append(pdf)

# Save the merged PDF
merger.write("merged-pdf.pdf")
merger.close()
