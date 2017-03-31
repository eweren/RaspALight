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

To make sure, that you have access to the LED functionality, you have to make sure, that pigpiod is running.
-> For example you can make a Cronjob for starting pigpiod at every boot-up:
    Therefore just type in:
      sudo nano /etc/crontab
      Add the following line to the end of the file:
      @reboot root pigpiod
  