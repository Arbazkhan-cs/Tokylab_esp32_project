# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from wifi import connect_to_wifi
from config import credentials
import os
from machine import SoftSPI, Pin
from sdcard import SDCard

ssid = credentials.get("ssid")
password = credentials.get("password")
groq_api_key = credentials.get("GROQ_API_KEY")
google_api_key = credentials.get("Google_API_KEY")
"""
try: 
    # Configure SPI and SD card
    spisd = SoftSPI(-1, miso=Pin(13), mosi=Pin(12), sck=Pin(14))
    sd = SDCard(spisd, Pin(26))

    # Mount SD card
    vfs = os.VfsFat(sd)
    os.mount(vfs, '/sd')
    os.chdir("/sd")
except Exception as e:
    print("OSError:", e)
"""
#connect_to_wifi(ssid, password)