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
3. Copy the [`kb.py`](kb.py) and [`main.py`](main.py) files.

Now customize the layout and features in [`main.py`](main.py) file, and save the updates on your board.

## Default layout

View the [Janus default layout on Keyboard Layout Editor](http://www.keyboard-layout-editor.com/#/gists/5144ea6a6c998df5f502f9240068de80)

This default layout is inspired by [Callum's QMK layout](https://github.com/qmk/qmk_firmware/tree/master/users/callum), with the following differences:

* Mods are moved to the bottom row on each layer, and are mirrored on both sides.
* No one-shot mods.
* Key layout is rearranged.