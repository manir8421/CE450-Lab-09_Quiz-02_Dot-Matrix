import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

row_pins = [2, 3, 4, 17, 24, 22, 10, 18]
col_pins = [25, 5, 6, 13, 8, 26, 27, 9]

for pin in row_pins + col_pins:
    GPIO.setup(pin, GPIO.OUT)

def clear_matrix():
    for row_pin in row_pins:
        GPIO.output(row_pin, GPIO.LOW)
    for col_pin in col_pins:
        GPIO.output(col_pin, GPIO.HIGH)

def display_letter_sequentially(pattern):
    for row in range(8):
        clear_matrix()
        GPIO.output(row_pins[row], GPIO.HIGH)
        
        for col in range(8):
            col_state = GPIO.LOW if pattern[row] & (1 << (7 - col)) else GPIO.HIGH
            GPIO.output(col_pins[col], col_state)
        
        time.sleep(0.001)

pattern_A = [
    0b00011000,
    0b00100100,
    0b01000010,
    0b01000010,
    0b01111110,
    0b01000010,
    0b01000010,
    0b01000010,
]

pattern_B = [
    0b11111000,
    0b11000100,
    0b11000010,
    0b11111100,
    0b11111100,
    0b11000010,
    0b11000100,
    0b11111000,
]

try:
    while True:
        for _ in range(200):
            display_letter_sequentially(pattern_A)
        
        for _ in range(200):
            display_letter_sequentially(pattern_B)

except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
