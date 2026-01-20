from scotiabank_cc_pdf_reader import ScotiabankPdfReader
from scotiabank_ctacte_parser import ScotiabankCuentaCorrienteParser

PDF_PATH = "/Users/ccanas/personal/python-projects/finance-test/pdfs/Scotiabank-01.pdf"


def main():
    reader = ScotiabankPdfReader(PDF_PATH)
    parser = ScotiabankCuentaCorrienteParser()

    pages = reader.extract_text_by_page()

    movimientos = parser.parse(pages)

    print(f"Movimientos detectados: {len(movimientos)}\n")

    for mov in movimientos[:10]:
        print(mov)


if __name__ == "__main__":
    main()