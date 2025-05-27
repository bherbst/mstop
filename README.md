# M-Stop
I was at an [FRC Team 2052 (KnightKrawler)](https://www.team2052.com/) while some programming students were iterating on the team's autonomous code, and I was thinking about the extra brake pedal for driving instructors in cars designed for driver's education. Wouldn't it be cool if we had an extra brake pedal (e-stop button) for FRC mentors?

Now we do!

<img src="/images/mstop.webp" height="400px" alt="Glowing red button mounted to a 3D printed cylindrical housing" />

## Okay but what _is_ it
The M-Stop is really just a Bluetooth space bar. That's it! 

## Materials
* 1x [3D printed body](https://github.com/bherbst/mstop/blob/main/models/MStop%20-%20Body.stl)
* 1x [3D printed bottom & electronics holder](https://github.com/bherbst/mstop/blob/main/models/MStop%20-%20Bottom.stl)
* 1x TinyS3 ESP32 board ([Adafruit](https://www.adafruit.com/product/5398))
    * You could definitely find a cheaper BLE board if you wanted to. The 3D printed mount is designed for the TinyS3.
* 1x Mini (24mm) arcade button ([Adafruit](https://www.adafruit.com/product/3430))
* 1x Mini on-off power button ([Adafruit](https://www.adafruit.com/product/3870))
* 1x battery (I used [this 3.7v, 400mAh one from Adafruit](https://www.adafruit.com/product/3898) and designed the 3D print for it, if you want to use something else you'll need to adjust how you install it)
* 1x Male JST PH cable ([Adafruit](https://www.adafruit.com/product/3814))
* Miscellaneous wires, solder, and connectors. The specifics here aren't super important. I decided to try out [a JST-PH connector](https://www.amazon.com/dp/B0731MZCGF) with [this 4-wire cable](https://www.adafruit.com/product/3891) to ease assembly, but you could also directly solder everything together if you wanted to.

## Wiring
1. Solder the red (+) wire from the JST-PH cable to one side of the on-off button
1. Solder a wire from the other side of the on-off button to VBAT on the TinyS3
1. Solder the black (-) cable from the JST-PH cable to the ground on the TinyS3
1. Solder the wires for your button (either directly or via a 3 wire JST cable if using) to ground, D6, and D7 on the TinyS3
  * Pin 6 will be the button input
  * Pin 7 will be the button's LED
1. Solder the wires to the button (or the other end of a JST cable, if using). If you're so inclined, you could also use [quick-connects](https://www.adafruit.com/product/3835) for this.
  * Note that the mini arcade button has two sets of terminals - the two that are perfectly aligned are for the LED, the two that are slightly offset are for the button
  * Bridge the two ground terminals with a short wire, then solder on the ground cable leading to the TinyS3
  * Connect the LED's positive terminal to pin 7 on the TinyS3
  * Connect the button's positive terminal to pin 6 on the TinyS3

The TinyS3 side of things will look like this when you're done:<br />
<img src="/images/electronics.webp" height="500px" />

And all the electronics together will look a bit like this:<br />
<img src="/images/all_electronics.webp" height="500px" />

## Assembly
1. Snap the TinyS3 and the on-off button into the 3D print<br /><img src="/images/internals_before_battery.webp" height="500px" />
1. Snap the battery into its slot and connect the JST PH cable<br /><img src="/images/internals.webp" height="500px" />
1. Attach the mini arcade button to the m-stop body. Unscrew the white threaded nut, insert the button into the body, and screw the nut back on. Unless you have unusually long and slender fingers, this is easiest to do by simply sticking a pen, screwdriver, or other such tool between the nut and the inside wall of the body and rotating the button itself until everything is tight.<br /><img src="/images/button_and_body.webp" height="500px" />
1. If you're using a JST cable for the button, connect that now
1. Screw the bottom with electronics into the body<br /><img src="/images/back.webp" height="500px" />

## Code
We will be using [CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython) to program the m-stop. I use VSCode with the CircuitPython extension, but you can use whatever CircuitPython IDE you'd like.
 
1. Connect the m-stop to a computer via a USB-C cable
1. Copy the contents from [`the /code/lib/` folder](https://github.com/bherbst/mstop/tree/main/code/lib) in this repo into the `/lib/` folder on the TinyS3
1. Replace the contents of the `code.py` file on your TinyS3 with the contents of [the `code.py` file](https://github.com/bherbst/mstop/blob/main/code/code.py) in this repo

## Using the M-Stop
Using the M-Stop is simple! Turn it on using the on-off button, then from the computer running the FRC Driver Station software connect to the M-Stop over Bluetooth (it should show up as `M-Stop`). 
The arcade button LED will flash when it is not connected, and will go solid once it has established a Bluetooth connection to something. It _should_ automatically reconnect to paired computers when powered on.

⚠️ **Warning:** I strongly recommend testing your M-Stop with a stationary robot before trying to use it while the robot is moving.
