from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
import board

keyboard = KMKKeyboard()

# 3 Rows: GP0, GP1, GP2
# 5 Cols: GP3 to GP7, with col 4 (GP7) for encoder switches
keyboard.row_pins = (board.GP0, board.GP1, board.GP2)
keyboard.col_pins = (board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# --- Encoders ---
encoder_handler = EncoderHandler()

# Encoder A/B pin pairs (NOT matrix)
encoder_handler.pins = (
    (board.GP8, board.GP9),     # Encoder 1
    (board.GP10, board.GP11),   # Encoder 2
    (board.GP12, board.GP13),   # Encoder 3
)

# What each encoder does when turned (on Layer 0)
encoder_handler.map = [
    (
        (KC.VOLD, KC.VOLU),     # Encoder 1
        (KC.LEFT, KC.RIGHT),    # Encoder 2
        (KC.MUTE, KC.MPLY),     # Encoder 3
    )
]

keyboard.modules.append(encoder_handler)

# --- Keymap: 3x5 matrix ---
# Cols 0–3 = normal switches
# Col 4 (GP7) = encoder switches
# e.g. Row 0, Col 4 = ENC1 SW

keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E, KC.R, KC.MUTE,   # Row 0
        KC.A, KC.S, KC.D, KC.F, KC.MPLY,   # Row 1
        KC.Z, KC.X, KC.C, KC.V, KC.ENT     # Row 2
    ]
]

# Launch
if __name__ == '__main__':
    keyboard.go()
