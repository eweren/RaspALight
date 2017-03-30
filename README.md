# RaspALight
A project making a smooth light-alarm clock with the help of a Raspberry Pi and LED light strips.


For setting up this project, you have to make sure, that:
1 - you have already installed a web server on your Pi (-> e.g follow this tutorial https://www.elektronik-kompendium.de/sites/raspberry-pi/1905271.htm)
2 - you have soldered or pinned the led strip to your GPIO-pins (-> the pins you used can be selected in the settings)
3 - you have pigpiod installed (-> http://abyz.co.uk/rpi/pigpio/download.html)

To finalize the project, you just have to go to your web server folder (/var/www/html/).
At this time, there should only be an index.html file. You can delete it an paste all the stuff of this repository into the html-folder.
After that, you should have the file index.html in there, as well as the folder ledcontrol.
Make sure that the user, the webserver is running on, has permission to read, write and execute files in there.

Now, you can already access your website. To customize it, you can upload and change the background via the website, and do the rest in the index.php and style.css files.

For you, to understand what i did there with all those files:
-   index.html    -> Just a forwarding site to the index.php
-   index.php     -> Handles the python processes, to see if there is already an alarm set up, generating the html file based on wether there are active alarms or not
-   upload.php    -> Very simple script to upload a new background and setting it up
-   init.php      -> Simple script for setting the standard vars for the pins, the duration and the cut-off time
-   alarm.py      -> Script to handle the alarm, the php script set up
-   killpython.py -> Kills the python-process with the id given by args
-   setColor.py   -> Sets red, green and blue led to the given args

For a slight demo, of how the side will look (all buttons without a function), you can go to https://eweren.github.io/RaspALight/
