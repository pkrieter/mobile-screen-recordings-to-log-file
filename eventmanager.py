import event

class EventManager:
    """ Class EventManager

    This class is responsible for keeping a list of event definitions
    of objects of the class Event. For testing this class contains
    30 test event definitions for Android 8 screen videos. These events
    have been tested with video material from a Google Pixel 2.
    """
    def __init__(self):
        self.eventList = []
        self.createTestEvents()

    def addEvent(self, event):
        self.eventList.append( event )

    def createTestEvents(self):
        """ Create a list of test event definitions

        In this method 30 events are defined to be checked against the video material.
        These are based on the Event class and are defined based on screenshots of GUI
        states. The examples below are all for Android 8 Oreo in FullHD resolution using
        screenshots from a Google Pixel 2.
        """
        #1 keyboard opened
        e1 = event.Event('keyboard opened',True)
        e1.addFixedPosition('events/keyboard_small.jpg', (0,1168,1080,1640), False, True) # small
        e1.addFixedPosition('events/keyboard_capital.jpg', (0,1168,1080,1640), False, True) # capitals
        self.addEvent(e1)
        
        #2 SMS chat opened, with Person X
        e2 = event.Event('SMS chat opened')
        e2.addFixedPosition('events/messages_chat.jpg', (40,65,100,205), False, True) # go back arrow left
        e2.addFixedPosition('events/messages_chat.jpg', (860,65,1080,205), False, True) # icons on the right in header
        e2.addsearchForText((180,85,750,158),'',False)
        self.addEvent(e2)
        
        #3 SMS message/chatlist opened
        e3 = event.Event('SMS message/chatlist opened')
        e3.addFixedPosition('events/messages.jpg', (0,65,1080,205), False, True) 
        e3.addFixedPosition('events/messages.jpg', (919,1640,1015,1730), False, True) 
        self.addEvent(e3)
        """
        #4 SMS starting a new conversation screen
        e4 = event.Event('SMS starting a new conversation screen')
        e4.addFixedPosition('events/new_conversation_screen.jpg', (40,65,100,205), False, True) # go back arrow left
        e4.addsearchForText((180,85,750,158),'New conversation',False)
        self.addEvent(e4)

        #5 Letter 'k' got pressed
        e5 = event.Event('Letter k got pressed')
        e5.addFixedPosition('events/keyboard_small.jpg', (0,1168,1080,1640), False, True) # small
        e5.addFixedPosition('events/new_conversation_screen.jpg', (815,1160,905,1460), False, True) # capitals
        self.addEvent(e5)

        #6 whatsapp, chatlist opened
        e6 = event.Event('whatsapp, chatlist opened')
        e6.addFixedPosition('events/whatsapp_list.jpg', (0,65,1080,327), False, True) # header
        e6.addFixedPosition('events/whatsapp_list.jpg', (919,1640,1015,1730), False, True) 
        self.addEvent(e6)

        #7 whatsapp chatlist, scrolled down
        e7 = event.Event('whatsapp chatlist, scrolled down')
        e7.addFixedPosition('events/whatsapp_liste_scroll.jpg', (0,65,1080,180), False, True) # header oben
        e7.addFixedPosition('events/whatsapp_list.jpg', (919,1640,1015,1730), False, True) 
        self.addEvent(e7)

        #8 whatsapp, chatlist active, unread messages
        e8 = event.Event('whatsapp, chatlist active, number of chats with new messages')
        e8.addFixedPosition('events/whatsapp_list_newmessages.jpg', (105,242,430,336), False, True) 
        e8.addsearchForText((321,258,350,288),'',True) # get number in buble 
        self.addEvent(e8)

        #9 whatsapp chat opened with person X
        e9 = event.Event('whatsapp chat opened')
        e9.addFixedPosition('events/whatsappchat.jpg', (750,65,1080,205), False, True) # icons on the right in header
        e9.addFixedPosition('events/whatsappchat.jpg', (0,65,70,205), False, True) # back arow in header
        e9.addsearchForText((180,85,750,158),'',False) # get text with name from chat header
        self.addEvent(e9)

        #10 whatsapp, using camera
        e10 = event.Event('whatsapp, using rear camera')
        e10.addFixedPosition('events/whatsapp_cam.jpg', (842,1600,902,1642), False, True)
        self.addEvent(e10)
        
        #11 whatsapp button for taking picture/video pressed 
        e11 = event.Event('whatsapp, button for taking picture or video pressed')
        e11.addFixedPosition('events/whatsapp_cam3.jpg', (0,1880,50,1920), False, True)
        e11.addFixedPosition('events/whatsapp_cam3.jpg', (0,0,50,50), False, True)
        e11.addFixedPosition('events/whatsapp_cam3.jpg', (1030,0,1080,50), False, True)
        e11.addFixedPosition('events/whatsapp_cam3.jpg', (1030,1880,1080,1920), False, True)
        self.addEvent(e11)

        #12 Instagram opened
        e12 = event.Event('Instagram opened')
        e12.addFixedPosition('events/instagram_feed.jpg', (400,60,690,180), False, True)
        self.addEvent(e12)

        #13 instagram, feed
        e13 = event.Event('Instagram, feed opened')
        e13.addFixedPosition('events/instagram_feed.jpg', (400,60,690,180), False, True)
        self.addEvent(e13)

        #14 instagram, feed, unread messages
        e14 = event.Event('Instagram, feed opened, unread messages')
        e14.addFixedPosition('events/instagram_feed.jpg', (400,60,690,180), False, True)
        e14.addFixedPosition('events/instagram_feed.jpg', (950,60,1080,185), False, True)
        self.addEvent(e14)

        #15 Instagram Directmessages Chat opened with: 
        e15 = event.Event('Instagram direct messages chat opened with')
        e15.addFixedPosition('events/instagram_directchat.jpg', (25,90,100,165), False, True)
        e15.addFixedPosition('events/instagram_directchat.jpg', (980,90,1055,165), False, True)
        e15.addsearchForText((110,90,970,165),'', False)
        self.addEvent(e15)

        #16 pinterest opened, chat with person X
        e16 = event.Event('Pinterest opened, chat with')
        e16.addFixedPosition('events/pinterest_chat.jpg', (25,90,100,165), False, True)
        e16.addFixedPosition('events/pinterest_chat.jpg', (950,90,1030,165), False, True)
        e16.addsearchForText((110,90,940,165),'', False)
        self.addEvent(e16)

        #17 BBC news openes, top stories present
        e17 = event.Event('BBC new open, viewing top stories')
        e17.addFixedPosition('events/bbc_news_top_stories.jpg', (360,63,720,200), False, True)
        e17.addFixedPosition('events/bbc_news_top_stories.jpg', (0,230,305,336), False, True)
        e17.addsearchForText((0,230,305,326), 'Top Stories', False)
        self.addEvent(e17)

        #18 home screen present
        e18 = event.Event('home screen present', True)
        e18.addFixedPosition('events/homescreen3.jpg',(96,1700,174,1777),False, True) # the G in google searchbar at the bottom, dark
        e18.addFixedPosition('events/homescreen.jpg',(96,1700,174,1777),False, True) # the G in google searchbar at the bottom, light
        self.addEvent(e18)

        #19 app menu present
        e19 = event.Event('app menu present', True)
        e19.addFixedPosition('events/appmenu.jpg',(95,120,175,200),False, True) # the G in google searchbar at the top
        self.addEvent(e19)

        #20 calculator present
        e20 = event.Event('Calculator present', True)
        e20.addFixedPosition('events/calculator.jpg', (0,700,1080,1790), False, True)
        e20.addFixedPosition('events/calculator.jpg', (0,700,1080,1790), True, True)
        self.addEvent(e20)

        #21 lockscreen present
        e21 = event.Event('lockscreen present')
        e21.addFixedPosition('events/lockscreen_2.jpg', (970,1810,1042,1878), True, True)
        self.addEvent(e21)

        #22 lockscreen present, notifications are there
        e22 = event.Event('lockscreen present, notifications are there1 ')
        e22.addFixedPosition('events/lockscreen_2.jpg', (970,1810,1042,1878), True, True)
        e22.addsearchForImage('events/lockscreen_2.jpg', (0,880,1080,930), 0.8, True) 
        self.addEvent(e22)

        #23 Contacts, list opened
        e23 = event.Event('Contacts, list opened')
        e23.addFixedPosition('events/contacts_list.jpg', (0,65,150,205), False, True) 
        e23.addFixedPosition('events/contacts_list.jpg', (860,65,1080,205), False, True) 
        e23.addsearchForText((150,65,750,205),'Contacts',False)
        self.addEvent(e23)

        #24 Contacts, editing a contact
        e24 = event.Event('Contacts, editing a contact')
        e24.addFixedPosition('events/contacts_edit.jpg', (0,65,1080,205), False, True) 
        e24.addFixedPosition('events/contacts_edit.jpg', (0,65,150,205), False, True)
        e24.addFixedPosition('events/contacts_edit.jpg', (840,65,1080,205), False, True) 
        self.addEvent(e24)

        #25 calling, trying to calling person X
        e25 = event.Event('calling, trying to call')
        e25.addFixedPosition('events/call_calling.jpg', (485,1600,596,1670), False, True)
        e25.addsearchForText((435,345,640,413),'Calling',False)
        e25.addsearchForText((0,420,1080,530),'', False) # get name of caller
        self.addEvent(e25)

        #26 calling, in call with
        e26 = event.Event('calling, in call with')
        e26.addFixedPosition('events/call_calling.jpg', (485,1600,596,1670), False, True)
        e26.addsearchForText((485,1272,590,1345),'Hold',True) # hold sign is only there if in call
        e26.addsearchForText((0,420,1080,530),'', False) # get name of caller
        self.addEvent(e26)

        #27 calling, hanging up, person X
        e27 = event.Event('calling, hanging up')
        e27.addFixedPosition('events/call_hangingup.jpg', (485,1600,596,1670), False, True)
        e27.addsearchForText((0,544,1080,603),'Hanging',False)
        e27.addsearchForText((0,420,1080,530),'', False) # get name of caller
        self.addEvent(e27)

        #28 incoming call, lock screen
        e28 = event.Event('incoming call lock screen')
        e28.addsearchForImage('events/call_incoming.jpg', (470,1500,600,1630), 0.8, True)
        e28.addsearchForText((425,120,650,195),'Call from',False)
        e28.addsearchForText((0,200,1080,360),'', False) # get name of caller
        self.addEvent(e28)

        #29 Smiley keyboard opened
        e29 = event.Event('Smiley keyboard opened')
        e29.addFixedPosition('events/keyboard_smiley.jpg', (294,1686,400,1784), False, True)
        self.addEvent(e29)

        #30 home button pressed
        e30 = event.Event('homebutton pressed', True)
        e30.addFixedPosition('events/homebutton.jpg', (492,1842,590,1871), True, True) 
        self.addEvent(e30)
        """

