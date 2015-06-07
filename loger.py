#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        log
# Purpose:
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import os
import logging
import sys

#path = '/opt/nsfocus/ATF/log'

class checklog():
    def __init__(self,filename):
        logging.basicConfig(level=logging.INFO,filemode='w')
        self.logger = logging.getLogger("") 
        #file = os.path.join(path,filename) 
        file = filename
        # create file handler which logs even debug messages
        fh = logging.FileHandler(file) 
        # create formatter and add it to the handlers
        formatter = logging.Formatter("%(message)s")
        fh.setFormatter(formatter)
        # add the handlers to logger
        self.logger.addHandler(fh)
        self.logger.setLevel(logging.WARNING)
       
    def debug(self,str):
        self.logger.debug(str)

    def error(self,str):
        self.logger.error(str)

    def info(self,str):
        self.logger.info(str)

    def exception(self,str):
        self.logger.exception(str)
        
    def warning(self,str):
        self.logger.warning(str)


def main():
    pass
#     ll = log('test.log')
#     ll.error("error")
#     ll.debug("debug")
#     ll.info("info")
#     ll.exception("exception")


if __name__ == '__main__':
    main()
