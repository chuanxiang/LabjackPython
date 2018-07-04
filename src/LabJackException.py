import ctypes

class LabJackException(Exception):
    """Custom Exception meant for dealing specifically with LabJack Exceptions.

    Error codes are either going to be a LabJackUD error code or a -1.  The -1 implies
    a python wrapper specific error.  
    
    WINDOWS ONLY
    If errorString is not specified then errorString is set by errorCode
    """
    def __init__(self, ec = 0, errorString = ''):
        self.errorCode = ec
        self.errorString = errorString

        if not self.errorString:
            try:
                pString = ctypes.create_string_buffer(256)
                staticLib.ErrorToString(ctypes.c_long(self.errorCode), ctypes.byref(pString))
                self.errorString = pString.value
            except:
                self.errorString = str(self.errorCode)
    
    def __str__(self):
          return self.errorString

