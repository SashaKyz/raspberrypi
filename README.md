# raspberrypi

Configure Raspberry Pi to use  UART Neo 6M GPS module

The Raspberry Pi has two built-in UARTs, a PL011 and a mini UART. They are implemented using different hardware blocks so they have slightly different characteristics. On the raspberry pi 3 however, the wireless/bluetooth module is connected to the PLO11 UART, while the mini UART is used for the linux console ouptut. Depending on how you see it, I will define the PLO11 as the best of the two UART due to its implementation level. So for this project we will be deactivating the Bluetooth module from the PLO11 UART using an overlay available in the updated current version of the Raspbian Jessie.

Now you have two option to keep UART port for GPS - use bluetooth port or use console port. 

#####TURN OFF THE BLUETOOTH
 
The first thing we will do under this is to edit the `/boot/config.txt` file. To do this, run the commands below:

`sudo nano /boot/config.txt`

at the bottom of the config.txt file, add the following lines

```
dtparam=spi=on
dtoverlay=pi3-disable-bt
core_freq=250
enable_uart=1
force_turbo=1
```
 
##### OR TURN OFF THE SERIAL CONSOLE
In older Raspberry Pi's, Raspbian uses the UART as a serial console. We need to turn off that functionality so that we can use the UART for our GPS module.

Backup the file before we start.

`sudo cp /boot/cmdline.txt /boot/cmdline_backup.txt`

The we need to edit cmdline.txt and remove the serial interface.

`sudo nano /boot/cmdline.txt`

If the file has `"console=ttyAMA0,115200"`, delete it, and save the file by pressing Ctrl X, Y, and Enter.

`sudo nano /etc/inittab`

Find ttyAMA0 by pressing Ctrl W and typing "ttyAMA0".

If it finds that line, insert a # symbol to comment out that line, and Ctrl X, Y, Enter to save.

Type `"sudo reboot"` to reboot the computer.

#####TRY IT OUT
To try out if the installation worked, type

`sudo cat /dev/ttyAMA0`

You should be seeing a lot of text pass by. That means it works. Type Ctrl + c to return.

#####INSTALLING SOFTWARE

We will be minicom to connect to the GPS module and make sense of the data. It is also one of the tools that we will use to test is our GPS module is working fine. An alternative to minicom is the daemon software GPSD.

`sudo apt-get install minicom`

To install GPSD software, type

`sudo apt-get install gpsd gpsd-clients`

Now run the gps client

`sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock`

Please note that it can take up to 30 minutes to get a GPS signal on the first run. The LED will be blink red when it has a connection.

#####INSTALLING LIBRARY

To easily parse the received data, we will make use of the pynmea2 library. It can be installed using;

`sudo pip install pynmea2`

Library documentation can be found here https://github.com/Knio/pynmea2

Installing the LCD Library:

For this tutorial we will be using the AdaFruit library. The library was made for AdaFruit screens but also works  for display boards using HD44780. If your display is based on this then it should work without issues.

I feel its better to clone the library and just install directly. To clone run;

`git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git`
 

change into the cloned directory and install it

```
cd ./Adafruit_Python_CharLCD
sudo python setup.py install
```
At this stage, I will suggest another reboot so we are ready to go on to connecting the components.



#### Connections for Raspberry Pi GPS module Interfacing:
[Wiring diagram](img/interfacing-GPS-module-with-Raspberry-pi-circuit-diagram.png)

##Sources:
1. https://pisavvy.com/neo-6m
2. https://circuitdigest.com/microcontroller-projects/raspberry-pi-3-gps-module-interfacing 