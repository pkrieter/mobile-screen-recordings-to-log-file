import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import imagehash
from scipy.misc import toimage
import datetime
import time

class MatchingManager:
    """ Class MatchingManager

    Provides methods related to match and find images with or in screenshots.
    """
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    def isInImage(self, searchIn, searchFor, threshold=0.8):
        """ Check if image is in screenshot

        Uses OpenCVs template matching algorithm to search for an image part
        in a screenshot.

        Args:
            searchIn: PIL image to search in
            searchFor: PIL image of image part to seach for
            threshold: decision threshold, default is 0.8

        Return:
            True, if the search image occured at least once in the screenshot, 
            otherwise False
        """
        img_gray = cv2.cvtColor(searchIn, cv2.COLOR_BGR2GRAY)
        template = cv2.cvtColor( cv2.cvtColor(np.array(searchFor), cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        locations = np.where( result >= threshold)
        if( len(locations[0]) > 0 ):
            return True
        else:
            return False

    def getPHashDistance(self, image1, image2):
        """  Calculate the similarity of two images

        Calculate and return the distance of perceptual hashes of two images.

        Args:
            image1:
            image2:
        """
        hash1 = imagehash.phash(image1)
        hash2 = imagehash.phash(image2)
        return hash1 - hash2

    def getEdgePHashDistance(self, image1, image2):
        return self.getPHashDistance( self.canny(image1), self.canny(image2) )

    def canny(self, image):
        edgedImage = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        edgedImage = cv2.GaussianBlur(edgedImage, (3, 3), 0)
        edgedImage = cv2.Canny(edgedImage, 225, 250)
        return Image.fromarray( edgedImage )