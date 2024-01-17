import PyPDF2 as pypdf


n=int(input("enter the number of pdf files you want to merge:-"))
files= []
pdf= ".pdf"
merger= pypdf.PdfMerger()


for i in range(n):
    pdfname=input('enter the names of pdf files:-')
    name = pdfname+pdf
    files.append(name)



for filename in files:
    pdffile = open(filename,"rb")
    reader = pypdf.PdfReader(pdffile)
    merger.append(reader)
pdffile.close()



folder_name = input("write the name of folder:-")
final=folder_name+pdf
merger.write(final)


