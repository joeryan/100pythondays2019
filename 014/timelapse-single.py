# take an image ever minute
# overwrite current image with new one
# adapted from the book
# Make: JUMPSTARTING Raspberry Pi Vision
# Sandy Antunes and James West
# Maker Media, Inc


import os
import time

delay = 10

directory = "/home/pi/web/"
filename = "spycam"
stem = ".jpg"
webfile = directory + filename + stem

mycommand = "raspistill -w 480 -h 640 -o"
# this is the actual 'do stuff' part. It runs forever
while True:
    runme = mycommand + " " + webfile
    os.system(runme)
    time.sleep(delay)
