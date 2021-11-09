import pywhatkit
text=input("Enter the text to convert into handwritten:")
pywhatkit.text_to_handwriting(text,"handwriting.jpg",[10,10,10])
