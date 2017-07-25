class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class ChannelError(Error):
    def __init__(self, chan):
        self.chan = chan

    def __str__(self):
        return "Invalid channel number " + repr(self.chan) + ". Enter valid channel number 1 or 2"
