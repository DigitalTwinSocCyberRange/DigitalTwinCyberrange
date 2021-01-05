import logging
import datetime
import os
import time

logging.basicConfig(filename='logs/plc5.log', format='%(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)
                                                
        # count = 0
    # while (count <= PLC_SAMPLES):
i=0
while i < 200:
        if (os.path.exists('logs/plc5.log')):
            print("ok", i)
            logging.debug("Everything is ok. ")
        
        else:
            print("not ok", i)
            filehandler = logging.FileHandler('logs/plc5.log', 'a')
            log = logging.getLogger()  # root logger - Good to get it only once.
            for hdlr in log.handlers[:]:  # remove the existing file handlers
                if isinstance(hdlr,logging.FileHandler): #fixed two typos here
                    log.removeHandler(hdlr)
            log.addHandler(filehandler)    
            
            logging.debug("Log file was deleted.")
            logging.debug("New log file created.")

        i=i+1
        time.sleep(1)
                