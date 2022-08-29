#!/usr/bin/env python
# coding: utf-8

# In[104]:


import io
import glob
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2 import PdfMerger
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A1
from collections import defaultdict

def Merge(X):
    #empty pdf list
    pdfs = []

    #get PDF list in current directory
    #pdf_list=glob.glob("*.pdf")
    #print(pdf_list)

    #Create io Bytes
    packet = io.BytesIO()
    # Create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=A1)
    #Specity Text Style
    can.setFont('Helvetica-Bold', 24)
    #Specify Coordinates and text
    can.drawString(890, 550, "Hello world")
    can.showPage()
    can.save()

    #Get Read PDF File
    file=open(X,'rb')
    readpdf=PyPDF2.PdfFileReader(file)

    #Grab total pages in file
    totalpages=readpdf.numPages

     # Move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    for i in range(totalpages):
        # Read your existing PDF
        existing_pdf = PdfFileReader(open(X, "rb"))
        output = PdfFileWriter()
        # Add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(i)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        outputStream = open(f"{i}_destination.pdf", "wb")
        output.write(outputStream)
        outputStream.close()
        pdfs.append(f"{i}_destination.pdf")

    #get PDF list in current directory
    pdf_list=glob.glob("*.pdf")

    #Merge Pdfs Together
    #Check merged PDFs
    #print(pdfs)
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(f"{X}_Merged.pdf")
    merger.close()

    #Delete individual pdf files
    for i in range(totalpages):
        if os.path.exists(f"{i}_destination.pdf"):
            os.remove(f"{i}_destination.pdf")

#Fetch list of PDFs in Current Directory
pdf_list=glob.glob("*.pdf")

#Run Merge function on all items in list
for i in pdf_list:
    Merge(i)


# In[ ]:





# In[103]:





# In[ ]:





# In[ ]:





# In[ ]:




