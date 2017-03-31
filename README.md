 # RaspALight
A project making a smooth light-alarm clock with the help of a Raspberry Pi and LED light strips.


For setting up this project, you have to make sure, that:
1 - you have already installed a web server on your Pi (-> https://www.elektronik-kompendium.de/sites/raspberry-pi/1905271.htm in combination with https://www.elektronik-kompendium.de/sites/raspberry-pi/1905281.htm for PHP5)
2 - you have soldered or pinned the led strip to your GPIO-pins (-> http://dordnung.de/raspberrypi-ledstrip/)
3 - you have pigpiod installed (-> http://abyz.co.uk/rpi/pigpio/download.html)

To finalize the project, you just have to go to your web server folder (/var/www/html/).
At this time, there should only be an index.html file. You can delete it an paste all the stuff of this repository into the html-folder.
After that, you should have the file index.html in there, as well as the folder ledcontrol.

Now, you can already access your website. to customize it, you can upload and change the background via the website, and do the rest in the index.php and style.css files.

For your understanding of what i did there with all those files:
-   index.html    -> Just a forwarding site to the index.php with a little preloading animation
-   index.php     -> Watches over the python processes, to see if there is already an alarm set up, generating the html file based on wether there are active alarms or not
-   upload.php    -> Very simple script to upload a new background and setting it up
-   alarm.py      -> Calculating when the alarm has to start, based on the data given by the index.php-forms and executing this alarm
-   killpython.py -> Kills the python-process with the id given by args
-   setColor.py   -> Sets red, green and blue led to the given args
