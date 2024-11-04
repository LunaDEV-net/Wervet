#  Copyright (c) 2024 by https://github.com/LunaDEV-net.
#  all rights reserved

class CustomError(Exception):
    """Base class for exceptions in this module."""
    pass

class EmptyDataError(CustomError):
    """Exception raised if data_in is empty.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="No data found (len(data_in) == 0) \n Please check the input data."):
        self.message = message
        super().__init__(self.message)

class EmptyColumnError(CustomError):
    """Exception raised for errors in the input data.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, line_num, message="Empty column found in line "):
        self.message = message + str(line_num)
        super().__init__(self.message)