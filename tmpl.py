#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import argparse
import re
import os
import time
import string
import difflib
import pdb
import traceback
from awesome_print import ap
from pprint import pprint as pp
from timeit import default_timer as timer
#3rd part package
from lxml import etree
from BeautifulSoup import BeautifulSoup
from twisted.internet import protocol, reactor
#Load custom library (remember to set PYTHONPATH in your .bashrc)

def main():
    try:
        pass
    except BaseException  as e:
        traceback.print_exc(file=sys.stdout)
        raise e
         
    pass

if __name__ == '__main__':
    start_time = timer()
    main()
    print("Elapsed time : %f " % (timer()-start_time))