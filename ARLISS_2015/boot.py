# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

import pyb
# pyb.main('nav_test.py') # main script to run after this one
# pyb.usb_mode('CDC+MSC') # act as a serial and a storage device
# pyb.usb_mode('CDC+HID') # act as a serial device and a mouse
# pyb.main('Final.py') # main script to run after this one
# pyb.main('test.py') # main script to run after this one
# boot.py -- runs on boot-up
pyb.LED(3).on()                 # indicate we are waiting for switch press
pyb.delay(2000)                 # wait for user to maybe press the switch
switch_value = pyb.Switch()()   # sample the switch at end of delay
pyb.LED(3).off()                # indicate that we finished waiting for the switch

pyb.LED(4).on()                 # indicate that we are selecting the mode

if switch_value:
    pyb.usb_mode('CDC+MSC')
    pyb.main('cardreader.py')
else:
    pyb.usb_mode('CDC+HID')
    pyb.main('Final.py')

pyb.LED(4).off()                # indicate that we finished selecting the mode
