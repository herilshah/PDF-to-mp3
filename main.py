import pyttsx3,PyPDF2
#Write your pdf name below
pdfreader = PyPDF2.PdfFileReader(open('sample.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print (clean_text)
#Your file will be saved as the file name below
speaker.save_to_file(clean_text, 'yourvoicefile.mp3')
speaker.runAndWait()

speaker.stop()