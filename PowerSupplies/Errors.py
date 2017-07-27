class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class ChannelError(Error):
    """Error is raised when user gives a channel other than 1 or 2"""

    def __init__(self, chan):
        self.chan = chan

    def __str__(self):
        return "Invalid channel number " + repr(self.chan) + ". Enter valid channel number 1 or 2"


class ChangeValueError(Error):
    """Error is raised when you intend to change a value but the readback indicates this didn't work"""

    def __init__(self, desiredVal, readVal):
        self.desiredVal = desiredVal
        self.readVal = readVal

    def __str__(self):
        return "You attempted to set a field to " + repr(self.desiredVal) + ", but the machine is still set to " + repr(self.readVal)
