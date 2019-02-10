import webbrowser

class JabberNotActiveError(Exception):
    """Raised when jabber is not active, hence the program should not run"""
    def __init__(self):
        super().__init__("There is no process running of Cisco Jabber")

class Jabber:
    def __init__(self):
        """Checks if cisco Jabber is working otherwise raises exception"""
        # if jabber process is running
        # self.mainJabberProcess = the id we get

    def call(self,phoneNumber):
        webbrowser.open("tel:"+phoneNumber)
        # self.callProcessID = processID of Jabber Call
        # return self.callProcessID

    def isCalling(self):
        # if self.callProcessID is active
        #  return True
        # else
        #  return False
