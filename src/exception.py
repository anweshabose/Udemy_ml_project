#(d:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\48-End To End ML Project\venv) 
# D:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\48-End To End ML Project>python -m src.exception

import sys # any exception that is catched, sys library will have its information
from src.logger import logging

def error_message_detail(error,error_detail:sys): # assume ":" as "="
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero Error")
        raise CustomException(e, sys)
# __main__.CustomException: Error occured in python script name [exception.py] line number [26] error message[division by zero]