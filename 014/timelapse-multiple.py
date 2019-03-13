# Spy-Pi code version 2
# takes an image every minute, and saves 1 week (7 days) of data
# it also makes the most current image available 
# adapted from the book
# Make: JUMPSTARTING Raspberry Pi Vision
# Sandy Antunes and James West
# Maker Media, Inc

import os
import time
import shutil
# choose a delay time in seconds by modifying the next line
delay = 30
filename = "spycam"
stem = ".jpg"
# also, this is the file the webserver expects
# this is the command to run.
mycommand = "raspistill -h 640 -w 480 --nopreview -o"
# this is the actual 'do stuff' part. It runs forever
while True:
    myfile = directory + filename + "_" + str(icount) + stem
    runme = mycommand + " " + myfile
    os.system(runme)
    time.sleep(delay)
        
