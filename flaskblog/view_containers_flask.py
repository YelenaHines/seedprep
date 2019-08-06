# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 13:00:29 2019

@author: YHINE
"""

import re
#import time
#import datetime
import pyperclip


#import logging
#import pandas as pd

'''This program is designed to find contianer ID patterns from the clipboard,
    and then launch google chrome > orion >
    view containers to view each match'''

ORIONLOTREGEX = re.compile(r'\d{8}-\d{3,4}')
MQTIDENTIFIER = re.compile('^2019')
REQUESTFORMAT = re.compile(r'\d{8}')
##display_of = re.compile(r'of \d+')

def perform_orion_function(function, username, password, request_id=None):

    from flaskblog.class_orion_functions import OrionFunctions

    '''Prompt the user to return a request ID. The function will search and
    find the containers associated with the request'''

    while True:

#        print('\n\nWelcome to Container Lookup. After entering request ID into the prompt, click the chrome window for the program to focus on.')
#        print('\nEnter "Q" to quit')
#        request_id = input('Request ID: ').lower()


        if function == "view":
            emp_x = OrionFunctions(username, password, request_id)
            emp_x.logon_orion()
            if request_id == None:
                return None
            else:
                emp_x.get_requests()
                check = emp_x.get_request_id(request_id)
                if check == False:
                    return None
                emp_x.open_shipTrans()
                text = str(pyperclip.paste())
                for groups in ORIONLOTREGEX.findall(text):
                    if MQTIDENTIFIER.search(groups) == None:
                        emp_x.matches.append(groups)
                emp_x.paste_container(emp_x.matches)

                return emp_x.close_driver()
        else:
            return




#        if request_id == 'q':
#            break

#        elif REQUESTFORMAT.search(request_id) != None:
#
#            orion.get_requests()
#            check = orion.get_request_id(request_id)
#            if check == False:
#                print('Invalid ID')
#                break
#            display_num = orion.get_display_of()
#            orion.open_shipTrans()
#
#            text = str(pyperclip.paste())
#            for groups in ORIONLOTREGEX.findall(text):
#                if MQTIDENTIFIER.search(groups) == None:
#                    matches.append(groups)
#
#            orion.paste_container(matches)
#
#            print('\nResults --')
#            orion.get_container_loc(matches)
#            print('\nTotal matches: {}/{}'.format(len(matches), display_num))
#
#            orion.close()
#
#            return len(matches)
#
#        else:
#            print('The request ID is invalid')


#if __name__ == '__main__':
##    START = time.time()
##    run_test_copy()
##    END = time.time()
##    DURATION = END - START
##    print('\nDuration: {}s'.format(DURATION))
#
#    perform_orion_function()
