import PyPDF2

pdf_files =["1.pdf" ,"2.pdf"]

merger =PyPDF2.PdfMerger()

for filename in pdf_files:
    pdf_files = open(filename ,'rb')
    pdfReader = PyPDF2.PdfReader(pdf_files)
    merger.append(pdfReader)

pdf_files.close()
merger.write('merged.pdf')