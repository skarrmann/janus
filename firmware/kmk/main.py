from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.split import Split
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

split = Split(
    data_pin = keyboard.data_pin,
    data_pin2 = keyboard.data_pin2,
    uart_flip = False
)

keyboard.modules = [split, Layers()]
keyboard.extensions = [MediaKeys()]

SYM = KC.MO(1)
NAV = KC.MO(2)
FUN = KC.MO(3)

keyboard.keymap = [
    [   # Default
        KC.Q,    KC.W,    KC.F,    KC.P,    KC.G,    KC.J,   KC.L,     KC.U,    KC.Y,   KC.QUOT,
        KC.A,    KC.R,    KC.S,    KC.T,    KC.D,    KC.H,   KC.N,     KC.E,    KC.I,   KC.O,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.K,   KC.M,     KC.COMM, KC.DOT, KC.SLSH,
                                   NAV,     KC.LSFT, KC.SPC, SYM
    ],
    [   # Symbol
        KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,
        KC.GRV,  KC.LPRN, KC.RPRN, KC.SCLN, KC.BSLS, KC.NO,   KC.EQL,  KC.LBRC, KC.RBRC, KC.MINS,
        KC.LGUI, KC.LALT, KC.LSFT, KC.LCTL, KC.NO,   KC.NO,   KC.RCTL, KC.RSFT, KC.RALT, KC.RGUI,
                                   FUN,     KC.TRNS, KC.TRNS, KC.TRNS
    ],
    [   # Navigation
        KC.PSCR, KC.INS,  KC.APP,  KC.DEL,  KC.NO,   KC.NO,   KC.HOME, KC.PGDN, KC.PGUP, KC.END,
        KC.ESC,  KC.TAB,  KC.ENT,  KC.BSPC, KC.NO,   KC.NO,   KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT,
        KC.LGUI, KC.LALT, KC.LSFT, KC.LCTL, KC.NO,   KC.NO,   KC.RCTL, KC.RSFT, KC.RALT, KC.RGUI,
                                   KC.TRNS, KC.TRNS, KC.TRNS, FUN
    ],
    [   # Function
        KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.NLCK, KC.SLCK, KC.F9,   KC.F10,  KC.F11,  KC.F12,
        KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.NO,   KC.CLCK, KC.MUTE, KC.VOLD, KC.VOLU, KC.PAUS,
        KC.LGUI, KC.LALT, KC.LSFT, KC.LCTL, KC.NO,   KC.NO,   KC.RCTL, KC.RSFT, KC.RALT, KC.RGUI,
                                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
    ]
]

if __name__ == '__main__':
    keyboard.go()