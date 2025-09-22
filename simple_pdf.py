from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

text = """Industry 4.0 is the ongoing automation of traditional manufacturing and industrial practices, 
using modern smart technology. Large-scale machine-to-machine communication (M2M) and the Internet of Things (IoT) 
are integrated for increased automation, improved communication and monitoring, and production of smart machines."""

pdf.multi_cell(0, 10, text)

pdf.output("sample.pdf")

print("sample.pdf created successfully!")