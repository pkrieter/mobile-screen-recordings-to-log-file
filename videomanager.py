import cv2
import numpy as np

class VideoManager:
    """ Class VideoManager

    This class reads a video file from given filepath and provides
    methods to get timestamps and to calculate frames differences.

    Attributes:
        pathToVideo: file path of video to be read

    """
    def __init__(self, pathToVideo):
        self.vidcap = cv2.VideoCapture(pathToVideo)
        #self.skip = framesToSkip
    
    def getNextVideoFrame(self):
        success,image = self.vidcap.read()
        return success,image

    def getTimeOfCurrentVideoFrame(self):
        timeStamp = self.vidcap.get(cv2.CAP_PROP_POS_MSEC)
        return timeStamp

    def checkFrameDifference(self, frameA,frameB):
        frameDiff = cv2.subtract(frameA,frameB)
        return np.max(frameDiff)

    def checkFrameDifferenceSumAver(self, frameA,frameB):
        frameDiff = cv2.subtract(frameA,frameB)
        resolution = np.shape( frameDiff )
        numberOfPixels = resolution[0] * resolution[1]
        return np.sum(frameDiff) / numberOfPixels
        