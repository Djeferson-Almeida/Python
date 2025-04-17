import PyPDF2

def PDFmerge(pdfs, output):
  pdf_merger = PyPDF2.PdfFileMerger()
   
  for pdf in pdfs: #Percorre os arquivos PDF
      pdf_merger.append(pdf) 
  with open(output,'wb') as f:
    pdf_merger.write(f)

def main():
   pdfs = ['',''] #Nome dos dois arquivos a serem combinados
   output = 'combined_example.pdf'
   PDFmerge(pdfs,output) 

main()