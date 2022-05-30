import pyttsx3
import PyPDF2
book = open('object_oriented_python_tutorial.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.getNumPages()
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(7)
text = page.extract_text()
speaker.say(text)
speaker.runAndWait()