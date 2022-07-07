from PyPDF2 import PdfWriter, PdfReader

watermark = PdfReader("wtr.pdf")
writer = PdfWriter()
reader = PdfReader("merged.pdf")
for page in reader.pages:
	page.merge_page(watermark.pages[0])
	writer.add_page(page)

with open("watermarked.pdf", "wb") as file:
	writer.write(file)
