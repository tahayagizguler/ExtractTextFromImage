#!/usr/bin/python3
from email.mime import image
import pytesseract
from PIL import Image
import os


# If you are using Windows, do the following configuration.
#pytesseract.pytesseract.tesseract_cmd = r"<full_path_to_your_tesseract_executable>"
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def multiple():
    folder = (input("path: "))
    for i in os.listdir(folder):
        file = f"{folder}{i}"
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif','.jfif','.webp')):
            img = Image.open(file)
            print("Processing Image... >>> "+ i)
            text = pytesseract.image_to_string(img)

            if len(text) >= 1:
                print("An text has been found and is being saved.\n")

                with open("savedtexts.txt","a", encoding='utf-8') as f:
                        forOutput = "\n" + 65 * "x" + "\n"
                        f.write(forOutput + i + forOutput)
                        f.write(text)
            else:
                print("No text was found.\n")

        else:
            print("Processing is failed. >>> " + i + " \nNot found or not an image file.\n")

def single():
        path = (input("path: "))
        if path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif','.jfif','.webg')):            
            img = Image.open(path)
            print(img.filename)
            print("Processing Image... >>> "+ path)
            text = pytesseract.image_to_string(img)
            if len(text) >= 1:
                print("An text has been found and is being saved.\n")

                with open("save.txt","a", encoding='utf-8') as f:
                    foroutput = "\n" + 65 * "x" + "\n"
                    f.write(foroutput + path + foroutput)
                    f.write(text)
            else:
                print("No text was found.\n")

        else:
            print("Processing is failed. >>> " + path + " \nNot found or not an image file.\n")

while 1:
    print("********** Basic Image Read System **********")
    print("1.Read Image ")
    print("2.Read Multiple Image ")
    print("3.Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        single()
    elif ch == 2:
        multiple()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")











