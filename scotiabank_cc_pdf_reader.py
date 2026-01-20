from pathlib import Path
from typing import List, Dict, Any
import pdfplumber


class ScotiabankPdfReader:
    """
    Responsible for extracting structured and unstructured data
    from bank statement PDFs using pdfplumber.
    """

    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)

        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF not found at: {self.pdf_path}")

        if self.pdf_path.suffix.lower() != ".pdf":
            raise ValueError("Provided file is not a PDF")

    def extract_text_by_page(self) -> List[str]:
        """
        Returns the full text of the PDF, separated by pages.
        """
        pages_text: List[str] = []

        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text() or ""
                    pages_text.append(text)

        except Exception as e:
            raise RuntimeError(f"Error reading PDF: {e}") from e

        return pages_text

    def extract_tables(self) -> List[List[List[str]]]:
        """
        Attempts to extract all tables from the PDF.
        Returns a list of tables (each table is a list of rows).
        """
        all_tables: List[List[List[str]]] = []

        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                for page in pdf.pages:
                    tables = page.extract_tables()
                    if tables:
                        all_tables.extend(tables)

        except Exception as e:
            raise RuntimeError(f"Error extracting tables from PDF: {e}") from e

        return all_tables