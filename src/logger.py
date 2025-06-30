#(d:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\48-End To End ML Project\venv) 
# D:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\48-End To End ML Project>python -m src.logger
 
import logging # Python’s built-in module for event tracking and debugging.
import os # Used for file path manipulations and directory creation.
from datetime import datetime # Helps generate a timestamp for naming the log file.

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"   # %month_%day_%Year_%Hour_%Minute_%Second
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
if __name__=="__main__":
    logging.info("Logging has started")