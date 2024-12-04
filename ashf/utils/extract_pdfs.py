import os
import PyPDF2
import django
import sys

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ashf.settings')
django.setup()

# Now you can import your Django models
from ashf.models import PapersContent

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

if __name__ == "__main__":
    directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), "pdfs")

    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            path = os.path.join(directory, filename)
            print(f"Extrayendo texto de: {filename}")

            try:
                extracted_text = extract_text_from_pdf(path)

                # Save the extracted text to the database
                papers_content = PapersContent(content=extracted_text)
                papers_content.save()

                print(f"Texto guardado en la base de datos para: {filename}")

            except Exception as e:
                print(f"Error procesando {filename}: {e}")
