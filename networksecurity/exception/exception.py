import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self, error_message,error_details:sys):
        self.message = error_message
        _,_,exc_tb = error_details.exc_info()
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.lineno = exc_tb.tb_lineno

    def __str__(self):
        return f"NetworkSecurityException: {self.message} (File: {self.file_name}, Line: {self.lineno})"
    
