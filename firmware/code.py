"""
Mt Choc v1.0 KMK Build
"""

import board
import busio
import displayio
import adafruit_imageload

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from display import Display

class MtChoc(KMKKeyboard):
    def __init__(self):
        # =============================================================
        # Scanner
        self.diode_orientation = DiodeOrientation.COL2ROW

        self.col_pins = (
            board.GP28,     # col-1 (left)
            board.GP27,
            board.GP26,
            board.GP16,
            board.GP17,
            board.GP18,
            board.GP19,
            board.GP20,
            board.GP21,
            board.GP22,
            board.GP2,
            board.GP3,
            board.GP4,
            board.GP5,      # col-14 (right)
        )

        self.row_pins = (
            board.GP0,      # row-1 (top)
            board.GP1,
            board.GP15,
            board.GP14,
            board.GP13,     # row-5 (bottom)
        )

        # =============================================================
        # Physical Layout
        self.coord_mapping = [
            0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13,
            14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
            28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
            56, 57, 58,     60, 61, 62,     64, 65, 66, 67, 68, 69
        ]

        # =============================================================
        # Extensions
        layer_ext = Layers()
        display_ext = Display(imgfile="/samurai_pinbadge.bmp", grid_rows=10, grid_columns=4)

        self.modules = [layer_ext, display_ext]

        # =============================================================
        # Keymap
        _______ = KC.TRNS
        XXXXXXX = KC.NO

        # Layers
        LOWER = KC.MO(1)
        RAISE = KC.MO(2)

        self.keymap = [
            [   # Base
                KC.ESC,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.MINUS,  KC.EQUAL,  KC.BSPC,
                KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.LBRC,   KC.RBRC,   KC.BSLS,
                KC.CAPS,  KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,   KC.ENT,
                KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.RSFT,   KC.UP,
                KC.LGUI,  KC.LALT,  KC.LCTRL,           KC.SPC,   KC.SPC,   KC.SPC,             LOWER,    RAISE,    KC.DEL,   KC.LEFT,   KC.DOWN, KC.RGHT,
            ],
            [   # Lower
                KC.GRV,   _______, _______,   _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,   _______,   _______,
                _______,  _______, _______,   _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,   _______,   _______,
                _______,  _______, _______,   _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,   _______,
                _______,  _______, _______,   _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,   _______,
                _______,  _______, _______,             _______,  _______,  _______,            _______,  _______,  _______,  _______,   _______,   _______,
            ],
            [   # Raise
                KC.TILD,  _______, _______,   _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,   _______,   _______,
                _______,  _______, _______,   _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,   _______,   _______,
                _______,  _______, _______,   _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,   _______,
                _______,  _______, _______,   _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,   _______,
                _______,  _______, _______,             _______,  _______,  _______,            _______,  _______,  _______,  _______,   _______,   _______,
            ],
        ]


if __name__ == '__main__':
    keyboard = MtChoc()
    keyboard.go()
