import PyPDF2

f = open ('example.pdf','rb')

pdf_reader = PyPDF2.PdfFileReader(f)
pdf_writer = PyPDF2.PdfFileWriter()

for pages in range(pdf_reader.numPages):
  pdf_writer(pdf_reader.getPage(page))

pdf_writer.encrypt('12345')
result_pdf = open('Comsenha.pdf','wb')
pdf_writer.write(result_pdf)