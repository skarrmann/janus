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
3. Copy the custom files:
    * [`kb.py`](kb.py)
    * [`main.py`](main.py)
    * [`oneshot_mod.py`](oneshot_mod.py)

Now customize the layout and features in [`main.py`](main.py) file, and save the updates on your board.

## Default layout

View the [Janus default layout on Keyboard Layout Editor](http://www.keyboard-layout-editor.com/#/gists/5144ea6a6c998df5f502f9240068de80)

This default layout is inspired by [Callum's QMK layout](https://github.com/qmk/qmk_firmware/tree/master/users/callum), with the following differences:

* Mods are moved to the bottom row on every layer, and are mirrored on both sides.
* Symbol layer only contains non-shifted symbol keys.
* General differences in key positions.

Both our layouts use custom oneshot mod implementations to better suit our preferences.

## Custom oneshot mod implementation

This custom oneshot mod implementation supports the following:

* Oneshot mods can be chained together. Pressing oneshot mods does not interrupt currently-held oneshot mods.
* All held oneshot mods are released at the same time. They all share the same `timeout` parameter. Pressing any oneshot mod key resets the timeout counter.
* Supports three release modes with the `release_mode` parameter:
    * `OneShotModReleaseMode.ON_INTERRUPT_PRESS`: Release oneshot mods when first interrupt key is pressed
    * `OneShotModReleaseMode.ON_INTERRUPT_RELEASE`: Release oneshot mods when any interrupt key is released
    * `OneShotModReleaseModeON_ALL_INTERRUPT_RELEASE`: Release oneshot mods when ALL interrupt keys are released
* Optionally supports the ability to cancel active oneshot mods by re-pressing the key with the `cancel_on_repress` parameter.
