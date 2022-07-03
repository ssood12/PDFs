import sys
import PyPDF2

inputs = sys.argv[1:]

def pdf_merger(inputs):
	merger = PyPDF2.PdfFileMerger()
	for pdf in inputs:
		merger.append(pdf)
	merger.write('merged.pdf')
	print('DONE!')

pdf_merger(inputs)