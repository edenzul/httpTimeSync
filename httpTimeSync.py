#!/usr/bin/python

import time
import os

import requests

start_time = time.time()

try:


    raw_req = requests.get('https://worldtimeapi.org/api/timezone/Asia/Taipei.json')
    date_time_elements = raw_req.json()
    ts = date_time_elements['unixtime']

    print('Return TS from server\t : %s' % ts)

    # calculate processing delay
    delta = time.time() - start_time
    print('Server response time \t : %s seconds' % delta)

    newts = ts + delta
    print('Apply TS to localhost\t : %s' % newts)

    # execute system datetime changes
    cmd = 'date +%s.%N -s @' + ("%s" % newts)
    os.system(cmd)

except:
    print('Could not sync with time provider.')

print('Done.')
