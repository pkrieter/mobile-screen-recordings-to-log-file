""" Logcreator
 
This file contains the main() function and executes the log file
creation using a list of events and a folder of screen recordings to create
log files of.
The detection works frame by frame using multiprocessing. The resulting
log file contains one or more log entries for every frame.
"""

import videomanager
import ocrmanager
import eventmanager
import matchingmanager
import logentry

from PIL import Image
import imagehash
from scipy.misc import toimage
import time
import multiprocessing as mp
import datetime
import glob
import os

import cv2
import numpy as np
from matplotlib import pyplot as plt

oManager = ocrmanager.OCRManager()
eManager = eventmanager.EventManager()
mManager = matchingmanager.MatchingManager()
logfile = {}
counter = 0 # global framecounter, over all videos
videoStarts = [] # contains the framenumbers at which a new video session starts
videoEnds = [] # contains the framenubers at which a video ends
numOfCores = mp.cpu_count()
skippedFrames = 0
usedframes = 0
isVideoProcessing = False

def addLogResult(entry):
    logfile[entry.frameCounter] = entry


def checkFrameForEvents(currentFrame, realFramePointOfTime, counter, eventList, orientation):
    entry = logentry.LogEntry(counter, realFramePointOfTime, orientation, False)
    currFrameRGBandIMG = Image.fromarray( cv2.cvtColor( currentFrame, cv2.COLOR_BGR2RGB ) )

    for event in eventList:

        appendToLogmessage = ''
        isEvent = True

        if event.fixedPositionList:
            wasTrueAtLeastOneTime = False # for OR events
            for fixedPositionImage in event.fixedPositionList:  
                if(isEvent or event.isOR):
                    eventImage = Image.open(fixedPositionImage['image']).crop(fixedPositionImage['positionAndSize'])
                    frameImage = currFrameRGBandIMG.crop(fixedPositionImage['positionAndSize']) #Image.fromarray( cv2.cvtColor( currentFrame, cv2.COLOR_BGR2RGB ) ).crop(fixedPositionImage['positionAndSize'])
                    
                    hash = 99 # just for inital value
                    if fixedPositionImage['useEdges']:
                        hash = mManager.getEdgePHashDistance( eventImage, frameImage )
                    else:
                        hash = mManager.getPHashDistance( eventImage, frameImage )
                    if(hash < 18):
                        isEvent = True
                        wasTrueAtLeastOneTime = True
                    else:
                        isEvent = False
            if event.isOR and wasTrueAtLeastOneTime:
                isEvent = True

        if( len(event.searchForImageList) > 0 and isEvent ):
            for searchForImage in event.searchForImageList:
                if(isEvent):
                    searchFor = Image.open(searchForImage['image']).crop(searchForImage['positionAndSize'])
                    isEvent = mManager.isInImage(currentFrame, searchFor, searchForImage['threshold'])
        
        if( len(event.searchForTextList) > 0 and isEvent ):
            for text in event.searchForTextList:
                if(isEvent):
                    frameImage = currFrameRGBandIMG.crop(text['positionAndSize']) 
                    if text['searchterm']:
                        isEvent = oManager.lookForString(frameImage,text['searchterm'])
                    else:
                        appendToLogmessage = ' - ' + str( oManager.getStringFromImage(frameImage, text['onlyDigits']) )
                        isEvent = True

        #add found event to eventlist for this frame       
        if(isEvent):
            #cv2.imwrite("frametest_" + str(counter) + "_" + event.logMessage + appendToLogmessage + ".jpg", currentFrame ) # for debugging: save frame with found event to disk
            entry.addEvent( event.logMessage + appendToLogmessage )
    
    # add no event found in case of no events
    if len(entry.foundEvents) == 0:
        #cv2.imwrite("frametest_" + str(counter) + "_" + "NOTHING FOUND.jpg", currentFrame ) # for debugging: save frame with no event to disk
        entry.addEvent( 'NOTHING FOUND' ) 

    return entry

# lookForEvents()
# Check given image against list of Events
def lookForEvents(eventList, videoFileName, videotimeStamp, videoOrientation):
    global counter
    global videoStarts
    global videoEnds
    global skippedFrames
    global usedframes
    global isVideoProcessing

    isVideoProcessing = True

    # prepare video and multiprocessing
    vManager = videomanager.VideoManager( videoFileName )
    pool = mp.Pool(numOfCores)
    isPortraitMode = videoOrientation # no functionality yet!
    videoStartTime = videotimeStamp
    
     # add start for this videosession
    videoStarts.append(counter)
 
    print('# starting to look for events ...')
    print('# Video file: '+videoFileName)
    t = time.time()

    if( len(eventList) > 0 ):
        isFrame, lastFrame = vManager.getNextVideoFrame()
        isFrame, currentFrame = vManager.getNextVideoFrame()
        
        while isFrame:
            frameDiffMax = vManager.checkFrameDifference(lastFrame, currentFrame)
            frameDiffAv = vManager.checkFrameDifferenceSumAver(lastFrame,currentFrame)
            currentFrameTime = vManager.getTimeOfCurrentVideoFrame()
            realFramePointOfTime = videoStartTime + currentFrameTime

            if frameDiffMax > 100 or frameDiffAv > 1 or counter == 0:
                pool.apply_async( checkFrameForEvents, args=(currentFrame, realFramePointOfTime, counter, eventList, isPortraitMode), callback =  addLogResult )
                usedframes = usedframes + 1
            else:
                # no significant diff between frames, add empty event, copy events from event before after multiprocessing
                addLogResult( logentry.LogEntry(counter, realFramePointOfTime, isPortraitMode, True) )
                #pool.apply_async( addLogResult, args=( logentry.LogEntry(counter, realFramePointOfTime, isPortraitMode, True) ) )
                skippedFrames = skippedFrames + 1

            lastFrame = currentFrame
            isFrame, currentFrame = vManager.getNextVideoFrame()
            counter = counter + 1

    pool.close()
    pool.join()

    # add video-end event
    videoEnds.append(counter-1)

    isVideoProcessing = False 

    print('# Time needed for processing (seconds): '+ str(time.time() - t) )
    print('# done with this video.')

def getTimeStampAndOrientation(filename):
    timeSeperator = 'time_'
    orientationSeperator = '_mode_'
    format = '.mp4'

    fileTimeStamp = filename[filename.find(timeSeperator)+len(timeSeperator):filename.find(orientationSeperator)]
    orientationMode = filename[filename.find(orientationSeperator)+len(orientationSeperator):filename.find(format)]

    if orientationMode == 'portrait':
        orientationMode = True
    else:
        orientationMode = False

    return int(fileTimeStamp), orientationMode

def writeArrayToFile(logFileArray, fileName):
     
    # copy logentries for dublicate frames from the frame before
     for key in logFileArray:
         keyBefore = key - 1
         if logFileArray[key].copy == True and keyBefore > -1:
                logFileArray[key].foundEvents = list(logFileArray[keyBefore].foundEvents)

     # add events for start and end frames
     addStartAndEndEvents()
     
     # write to file
     logFile = open( fileName + '.txt', 'w' )
     
     # add line for CSV
     firstLineCSV = 'framenumber;timestamp;datenandtime;portraitmode;logmessage'
     seperator = ';'
     logFile.write( firstLineCSV + '\n')

     # add logentries
     i = 0;
     while i < len(logFileArray):
         entry = logFileArray[i]
         for logMessage in entry.foundEvents:
             logFile.write( str(entry.frameCounter) + seperator
                           + str(entry.timeStamp) + seperator
                           + str( getReadableTime(entry.timeStamp) ) + seperator
                           + str(entry.orientation) + seperator
                           + logMessage + '\n')
         i = i+1

     logFile.close()

def getReadableTime(realFramePointOfTime):
    return datetime.datetime.fromtimestamp( realFramePointOfTime / 1000 ).strftime('%Y-%m-%d %H:%M:%S.%f')

def addStartAndEndEvents():
    for startFrame in videoStarts:
        logfile[startFrame].foundEvents.insert(0,'VIDEO START FRAME')

    for endFrame in videoEnds:
        logfile[endFrame].foundEvents.insert(0,'VIDEO END FRAME')

def main():
    global logfile
    global isVideoProcessing

    # Format of videos file names: time_1512739679_mode_portrait.mp4
    folderName = 'test_videos' # change to folder containing video files
    path = os.getcwd() + '/' + folderName
    format = '.mp4'
    filesInFolder = glob.glob(os.path.join(path, '*'+format))

    for filename in filesInFolder:
        fileTimeStamp, orientationMode = getTimeStampAndOrientation(filename)
        lookForEvents(eManager.eventList, filename, fileTimeStamp, orientationMode)
    
    # done, write to logfile, but wait til last frame is processed, check multiprocessing again
    print( '################## ' + str(isVideoProcessing) )
    if not isVideoProcessing:
        writeArrayToFile( logfile, 'logfile_' + folderName )

    print('# Total number of frames (overall videos): ' + str(counter))
    print('# Number of skipped frames (overall videos): ' + str(skippedFrames))
    
if __name__=='__main__':
    main()


