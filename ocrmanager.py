from PIL import Image
import pytesseract
import time

class OCRManager:
    """ Class OCRManager

    Contains the path and config to tesseract for optical character recognition
    and methods for looking and getting strings from images. Please check 
    https://github.com/madmaze/pytesseract if you need help to configure the 
    path variables.

    """
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Tesseract-OCR\\tesseract.exe'
        # Include the above line, if you don't have tesseract executable in your PATH
        # Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
         
        tessdata_dir_config = '--tessdata-dir "C:\\Tesseract-OCR\\tesseract.exe\\tessdata"'
        # Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
        # It's important to add double quotes around the dir path.
    
    def lookForString(self, image, searchFor):
        """ Check if search string exists in image

        Args:
            image: PIL image to search in
            searchFor: string of text to search for in image
        Returns:
            True or False for string is in image or not
        """
        textInImage = pytesseract.image_to_string(image,  boxes=False ) #config="hocr"))
        isInImage = textInImage.find( searchFor )
        if( isInImage > -1 ):
            return True
        else:
            return False

    def getStringFromImage(self, image, onlyDigits=False):
        """ Get string from image and return it

        Args:
            image: PIL image to get text from
            onlyDigits: boolean, only search for digits instead of text and digites
        Returns:
            Found text string from image
        """
        if onlyDigits:
            return pytesseract.image_to_string(image,  boxes=False, config="single_digits" )
        else:
            return pytesseract.image_to_string(image,  boxes=False, config="abc" )
