class LogEntry:
    """ Class LogEntry

    This class defines the data structure of log entries. 

    Attributes:
        self: frame number of this log entry
        frameCounter: timestamp of this frame
        timeStamp: screen orientation of the video
        orientation: should we copy the eventlist from the frame before, because nothing changed?
        copy: list of found events for this frame
    """
    def __init__(self, frameCounter, timeStamp, orientation, copy):
        self.frameCounter = frameCounter  
        self.timeStamp = timeStamp
        self.orientation = orientation   
        self.copy = copy
        self.foundEvents = []             

    def addEvent( self, eventString ):
        self.foundEvents.append( eventString )
