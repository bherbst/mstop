import time
import board
import neopixel
import tinys3
from digitalio import DigitalInOut, Direction, Pull

import adafruit_ble
from adafruit_ble.advertising import Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard.hid import HIDService
from adafruit_ble.services.standard.device_info import DeviceInfoService
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

print("Booting M-Stop")
print("Battery voltage: {:.2f}".format(tinys3.get_battery_voltage()))

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3, auto_write=True, pixel_order=neopixel.GRB)
tinys3.set_pixel_power(True)

estop_button = DigitalInOut(board.D6)
estop_button.direction = Direction.INPUT
estop_button.pull = Pull.UP

estop_led = DigitalInOut(board.D7)
estop_led.direction = Direction.OUTPUT

hid = HIDService()
advertisement = ProvideServicesAdvertisement(hid)
# Advertise as "Keyboard" (0x03C1) icon when pairing
# https://www.bluetooth.com/specifications/assigned-numbers/
advertisement.appearance = 961
scan_response = Advertisement()
scan_response.complete_name = "M-Stop"

ble = adafruit_ble.BLERadio()
ble.name = "M-Stop"

if not ble.connected:
    ble.start_advertising(advertisement, scan_response)

keyboard = Keyboard(hid.devices)
while True:
    while not ble.connected:
        pixel[0] = ( 200, 100, 0, 0.1)
        estop_led.value = True
        time.sleep(0.4)
        estop_led.value = False
        time.sleep(0.4)

    while ble.connected:
        pixel[0] = ( 0, 255, 0, 0.5)
        estop_led.value = estop_button.value
        if not estop_button.value: # pull up means button pressed = false
            keyboard.send(Keycode.SPACEBAR)
            time.sleep(0.1)

    ble.start_advertising(advertisement, scan_response)