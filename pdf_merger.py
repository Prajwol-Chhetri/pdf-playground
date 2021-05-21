import sys
import PyPDF2

inputs = sys.argv[1:]  # taking the name of pdfs to be combined

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()  # creating a merger object of the PyPdf2 
	for pdf in pdf_list:
		merger.append(pdf)  # appending the contents of each pdf to merger
	merger.write('Merged.pdf')  # writing the merged contents to a new merged pdf

pdf_combiner(inputs)
