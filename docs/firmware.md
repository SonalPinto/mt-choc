# Firmware

The [Waveshare-RP2040-LCD-1.28](https://circuitpython.org/board/waveshare_rp2040_lcd_1_28/) is now supported by CircuitPython, as of the 8.0.0 release. Mt. Choc uses [KMK](http://kmkfw.io/) for firmware, same as [Purple Owl](https://github.com/SonalPinto/purple-owl).

## Instructions
- Get CircuitPython installed on the RP2040-LCD board.
- Unzip lib to extract the dependancy modules and copy them over to the CircuitPython/lib directory. This includes KMK.
- Copy `code.py`, `boot.py` and `display.py` into the CircuitPython drive.
- ???
- Profit 💸

## Dependancies
These modules are required aside from the native CircuitPython modules. A bundle with these modules precompiled is available in the as [lib.zip](../firmware/lib.zip) in the firmware directory. These modules need to placed within the `lib` directory of the CircuitPython drive.
- [KMK]((http://kmkfw.io/)
- [adafruit_imageload](https://github.com/adafruit/Adafruit_CircuitPython_ImageLoad)

## Boot
The [`boot.py`](../firmware/boot.py) by default will only enumerate the USB HID device. To enter into CircuitPython dev mode with various USB enumerations and access to the RP2040 storage, press ESC as the keyboard is powered on.

## Keyboard
Mt Choc runs on KMK. It is astoundingly simple to use and configuring even the wildest keyboards. The layout mapping for the diode matrix is defined in the `code.py`[../firmware/code.py] which also enumerates the `Display`(../firmware/display.py) for the pin badge.

## Pin Badge

The diplay glitch animation is a nifty trick played with CircuitPython displayio.TileGrid. The a reel of frames is loaded in as a bitmap, where each frame is 160x180ps. The below reel has 4 frames collated into a bitmap of 640x180.

<p align="center" width="100%">
    <img src="../assets/samurai_pinbadge.png">
</p>

A TileGrid is setup across a space of 160x180px with say, 1 column and 10 rows, and the larger bitmap is bound to it. Therefore, across the entire bitmap, there are (1 * 4) * 10 = 40 tiles! Though only 10 of these are in the "visible" at any point of time. The animation effect randomly swaps out the tiles across the frames, every cycle.

The `Display` module is not entirely generic, but it isn't too specific either. So it is possible to load a bitmap reel with more frames (as long as it can be loaded into memory) or go wild with the glitch effect configuration. Do ensure that the bitmap is paletted and using few colors (<=16).

Initially, I had wanted to entirely procedurally generate the glitch effect on the fly by sampling some coherent noise and using displacement maps across the channels. However, after playing with CircuitPython and the display, I ran in to the hard wall of what was realistically computable on a RP2040 running CircuitPython. As of right now, CircuitPython uses only one core of the RP2040. It would have been nice to have KMK on one core and the display animation and management on another core. Fancier things are clearly possible on the RP2040, no doubt - as evidenced by the [PicoSystem](https://shop.pimoroni.com/en-us/products/picosystem). But that trades off the utter convinience of KMK and CircuitPython, which I am not willing to let go of yet.

## QMK
You could possibly run QMK on this. Afterall, it's just an RP2040. Not too sure about the display though, since I haven't dabbled with QMK.
