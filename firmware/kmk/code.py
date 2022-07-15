import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D4,board.D5,board.D8,board.D9,board.D10)
keyboard.row_pins = (board.D0,board.D1,board.D2,board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

split = Split(
    split_flip=True,
    split_side=None,
    split_type=SplitType.UART,
    split_target_left=True,
    uart_interval=20,
    data_pin=board.D7,
    data_pin2=board.D6,
    uart_flip=False
)
keyboard.modules.append(split)

keyboard.keymap = [
    [
        KC.Q,  KC.W,  KC.F,  KC.P,   KC.G,    KC.J,   KC.L,    KC.U,    KC.Y,   KC.QUOT,
        KC.A,  KC.R,  KC.S,  KC.T,   KC.D,    KC.H,   KC.N,    KC.E,    KC.I,   KC.O,
        KC.Z,  KC.X,  KC.C,  KC.V,   KC.B,    KC.K,   KC.M,    KC.COMM, KC.DOT, KC.SLSH,
        KC.NO, KC.NO, KC.NO, KC.DEL, KC.LSFT, KC.SPC, KC.BSPC, KC.NO,   KC.NO,  KC.NO
    ]
]

if __name__ == '__main__':
    keyboard.go()