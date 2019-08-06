from PyPDF2 import PdfFileReader, PdfFileWriter
import glob
import sys
 
pdfs = glob.glob("*.pdf")
for pdf in pdfs:
	inputpdf = PdfFileReader(file(pdf, "rb"))
	if (inputpdf.numPages/4)==(float(inputpdf.numPages)/4.0):
		for i in range(inputpdf.numPages // 4):
			output = PdfFileWriter()
			if i==0:
				output.addPage(inputpdf.getPage(i))
			output.addPage(inputpdf.getPage(i * 4+1))
			output.addPage(inputpdf.getPage(i * 4+2))
			output.addPage(inputpdf.getPage(i * 4+3))
			output.addPage(inputpdf.getPage(i * 4+4))
			newname = pdf[:7] + "-" + str(i) + ".pdf"
			outputStream = file(newname, "wb")
			output.write(outputStream)
			outputStream.close()
	else:
		i=0
		for i in range(inputpdf.numPages // 4):
			output = PdfFileWriter()
			if i==0:
				output.addPage(inputpdf.getPage(i))
			output.addPage(inputpdf.getPage(i * 4+1))
			output.addPage(inputpdf.getPage(i * 4+2))
			output.addPage(inputpdf.getPage(i * 4+3))
			output.addPage(inputpdf.getPage(i * 4+4))
			newname = pdf[:7] + "-" + str(i) + ".pdf"
			outputStream = file(newname, "wb")
			output.write(outputStream)
			outputStream.close()
		i=i*4+4
		for i in range(inputpdf.numPages):
			output = PdfFileWriter()
			output.addPage(inputpdf.getPage(i))
		newname = pdf[:7] + "-" + str(i) + ".pdf"
		outputStream = file(newname, "wb")
		output.write(outputStream)
		outputStream.close()
