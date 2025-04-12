import PyPDF2

pdf_file = open(r'D:\Python_estudo\PDF\Note.pdf','rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
print(len(pdf_reader.pages))
page_obj = pdf_reader.pages[0]
print(page_obj.extract_text())
pdf_file.close()
