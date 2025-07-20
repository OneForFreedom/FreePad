import board
import digitalio

# Optional: Set status LED as output
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
