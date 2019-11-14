#!/usr/bin/env python3

import serial
import pynmea2

port = "/dev/ttyAMA0"  # the serial port to which the pi is connected.

def parseGPS(str):
    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)
        print("Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s -- Satellites: %s" % (
        msg.timestamp, msg.lat, msg.lat_dir, msg.lon, msg.lon_dir, msg.altitude, msg.altitude_units, msg.num_sats))


str="$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D"
parseGPS(str)
exit(0)

serialPort = serial.Serial(port, baudrate=9600, timeout=0.5)
while True:
    str = serialPort.readline()
    parseGPS(str)
