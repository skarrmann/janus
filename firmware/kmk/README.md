# Janus KMK Firmware

## Installation instructions

Apply these steps on each XIAO RP2040:

1. Install CircuitPython:
    * https://circuitpython.org/board/seeeduino_xiao_rp2040/
2. Following [KMK's split keyboard drive name convention](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/split_keyboards.md#drive-names), rename the `CIRCUITPY` drive to indicate whether it's the left or right side:
    * Left: `JANUS_L`
    * Right: `JANUS_R`
2. Copy KMK firmware files:
    * https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/Getting_Started.md
3. Copy the custom files:
    * [`kb.py`](kb.py)
    * [`main.py`](main.py)
    * [`oneshot_mod.py`](oneshot_mod.py)

Now customize the layout and features in [`main.py`](main.py) file, and save the updates on your board.

## Default keymap

View the [Janus default keymap on Keyboard Layout Editor](http://www.keyboard-layout-editor.com/#/gists/5144ea6a6c998df5f502f9240068de80)

This default keymap is inspired by [Callum's QMK keymap](https://github.com/qmk/qmk_firmware/tree/master/users/callum), with the following differences:

* Mods are moved to the bottom row on every layer, and are mirrored on both sides.
* Symbol layer only contains non-shifted symbol keys.
* General differences in key positions.

Both layouts use similar oneshot key implementations.

## Custom oneshot module

As part of the oneshot module's setup, the following two methods should be called:

* `set_ignore_keys(ignore_keys)`: Specify a list of keys which are not treated as oneshot interrupt keys

Oneshot keys behave as follows:

* When a oneshot key is pressed:
    * Set oneshot status as "active"
    * Send a key press event for its corresponding key
* When a oneshot key is released:
    * If oneshot status is "active", then set this oneshot key's status as "queued"
    * If oneshot status is not "active", send a key release event for its corresponding key
* When an interrupt key (i.e., not a oneshot key and not an ignored key) is pressed:
    * Set oneshot status as "inactive"
    * For every oneshot key with status "queued", send key release event for their corresponding key
    * Clear all oneshot key statuses