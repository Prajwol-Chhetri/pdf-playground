import sys
import PyPDF2

template_file = sys.argv[1] # name of the pdf file to watermark

template = PyPDF2.PdfFileReader(open(template_file, 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

with open('watermarked_pdf.pdf', 'wb') as file:
	output.write(file)