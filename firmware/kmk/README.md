# Janus KMK Firmware

## Installation instructions

Apply these steps on each XIAO RP2040:

1. Install CircuitPython:
    * https://wiki.seeedstudio.com/XIAO-RP2040-with-CircuitPython/
2. Following [KMK's split keyboard drive name convention](https://github.com/KMKfw/kmk_firmware/blob/master/docs/split_keyboards.md#drive-names), rename the `CIRCUITPY` drive to indicate whether it's the left or right side:
    * Left: `JANUS_L`
    * Right: `JANUS_R`
2. Copy KMK firmware files:
    * https://github.com/KMKfw/kmk_firmware/blob/master/docs/Getting_Started.md
3. Copy the [`code.py`](code.py) file.

Now customize the layout definition and features in this `code.py` file. Do whatever you want, this is just a simple starting point. Have fun!