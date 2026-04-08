import os
from fpdf import FPDF

def create_pdf(content, filename="output/result.pdf"):
    # create folder automatically
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # remove unsupported characters
    content = content.encode("latin-1", "ignore").decode("latin-1")

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    for line in content.split("\n"):
        pdf.multi_cell(0, 8, line)

    pdf.output(filename)