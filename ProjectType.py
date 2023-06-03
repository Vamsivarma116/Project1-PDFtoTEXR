# import PyPDF2
 
# #create file object variable
# #opening method will be rb
# pdffileobj=open('C:\\Users\\Dell\\Desktop\\sample.pdf','rb')
 
# #create reader variable that will read the pdffileobj
# pdfreader=PyPDF2.PdfFileReader(pdffileobj)


# # reader.pages[0]    # do not use this before decrypt
# # if pdfreader.isEncrypted:
# #     pdfreader.decrypt('')
# # pdfreader.pages[0]
 
# #This will store the number of pages of this pdf file




# x=pdfreader.numPages

# pdfreader.decrypt('sample')
 
# #create a variable that will select the selected number of pages
# pageobj=pdfreader.getPage(0)
 
# #(x+1) because python indentation starts with 0.
# #create text variable which will store all text datafrom pdf file
# text=pageobj.extractText()
 
# #save the extracted data from pdf to a txt file
# #we will use file handling here
# #dont forget to put r before you put the file path
# #go to the file location copy the path by right clicking on the file
# #click properties and copy the location path and paste it here.
# #put "\\your_txtfilename"
# file1=open(r"C:\\Users\\Dell\\Desktop\\1.txt","a")
# file1.writelines(text)
# file1.close()

from pdfminer.high_level import extract_text

text = extract_text('C:\\Users\\Dell\\Desktop\\sample.pdf')
print(text)

file1=open(r"C:\\Users\\Dell\\Desktop\\1.txt","a")
file1.writelines(text)
file1.close()

