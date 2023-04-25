
import cv2
from pytesseract import pytesseract
from PIL import Image

camera = cv2.VideoCapture(0)

while True:
    _,image = camera.read()
    cv2.imshow('Text detection', image)
    if cv2.waitKey(1) & 0xFF==ord('s'):
        cv2.imwrite('test1.jpg', image)
        break
camera.release()
cv2.destroyAllWindows()

def tesseract():
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract"
    Imagepath = 'test1.jpg'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(Imagepath))
    print(text[:-1])
tesseract()

# import pytesseract as tess
# tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# from PIL import Image
#
# img = Image.open('textHand.png')
# text = tess.image_to_string(img)
#
# print(text)