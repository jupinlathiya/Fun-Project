import pyttsx3
import PyPDF2

book=open('oops.pdf','rb')
pdfReager =PyPDF2.PdfFileReader(book)
pages=pdfReager.numPages
# print(pages)
speaker =pyttsx3.init()
for num in range(10,pages):
    page = pdfReager.getPage(num)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()