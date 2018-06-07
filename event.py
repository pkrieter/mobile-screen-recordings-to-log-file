import cv2
import numpy as np

class Event:
    """ Class Event

    An event definition is based on one or screenshots to define the GUI state  
    we are searching for and contains of three lists: for fixed positions of a GUI
    screen, for searching image parts and for searching and fetching text in 
    screen areas.

    Attributes:
        message: String of the log message to be written to the file for this event
        isOR: boolean expressing if only one condition of this event has to be 
              true (true) or all conditions have to be true (false)

    """
    def __init__(self, message, isOR=False):

        self.fixedPositionList = []   # compare region of given screenshot with fixed region of video frames
        self.searchForImageList = []  # search for image in frame or an optional region of the frame
        self.searchForTextList = []   # search for text in region of image
        self.logMessage = message     # log message of this event
        self.isOR = isOR              # are these 

    def addFixedPosition( self, image, positionAndSize, useEdges, condition ):
        self.fixedPositionList.append({
                        'image': image,
                        'positionAndSize': positionAndSize, # example: (0,0,100,220) to specify a rectangle area from pixel 0,0 to 100,220
                        'useEdges':useEdges,
                        'condition': condition # has no function right now
                        })

    def addsearchForImage( self, image, positionAndSize, threshold, region ):
        self.searchForImageList.append({
                        'image': image,
                        'positionAndSize': positionAndSize, # example: (0,0,100,220) to specify a rectangle area from pixel 0,0 to 100,220
                        'threshold': threshold,
                        'region': region
                        })

    def addsearchForText( self, positionAndSize, searchterm, onlyDigits ):
        self.searchForTextList.append({
                        'positionAndSize': positionAndSize, # example: (0,0,100,220) to specify a rectangle area from pixel 0,0 to 100,220
                        'searchterm':searchterm, # is search term is empty, get text from this region and attach to logmessage
                        'onlyDigits':onlyDigits
                        })