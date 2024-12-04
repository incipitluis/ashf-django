import os
import PyPDF2
from django.core.management import setup_environ
from ashf import settings 
from ashf.models import PapersContent 

# Configuración de Django (esto es necesario si el script se ejecuta fuera de Django)
setup_environ(settings)

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

if __name__ == "__main__":
    directory = "pdfs"

    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            path = os.path.join(directory, filename)
            print(f"Extrayendo texto de: {filename}")

            try:
                extracted_text = extract_text_from_pdf(path)

                # Guardar el texto extraído en la base de datos
                papers_content = PapersContent(content=extracted_text)
                papers_content.save()

                print(f"Texto guardado en la base de datos para: {filename}")

            except Exception as e:
                print(f"Error procesando {filename}: {e}")
