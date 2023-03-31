import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Define the GPIO pins for each segment of the display
segments = [8, 10, 12, 16, 18, 22, 24]

# Define the GPIO pins for the common anode/cathode pins of the display
# Change these to match your wiring if needed
com_anode_pin = 26
com_cathode_pin = 28

# Set up the GPIO pins for output
GPIO.setup(segments, GPIO.OUT)
GPIO.setup(com_anode_pin, GPIO.OUT)
GPIO.setup(com_cathode_pin, GPIO.OUT)

# Define the characters to display on the 7 segment display
# Change these to match the characters you want to display
digits = {
    '0': [1, 1, 1, 1, 1, 1, 0],
    '1': [0, 1, 1, 0, 0, 0, 0],
    '2': [1, 1, 0, 1, 1, 0, 1],
    '3': [1, 1, 1, 1, 0, 0, 1],
    '4': [0, 1, 1, 0, 0, 1, 1],
    '5': [1, 0, 1, 1, 0, 1, 1],
    '6': [1, 0, 1, 1, 1, 1, 1],
    '7': [1, 1, 1, 0, 0, 0, 0],
    '8': [1, 1, 1, 1, 1, 1, 1],
    '9': [1, 1, 1, 1, 0, 1, 1]
}

# Define a function to display a character on the 7 segment display
def display_digit(digit):
    # Set the common anode/cathode pin to the appropriate value
    GPIO.output(com_anode_pin, GPIO.HIGH)
    GPIO.output(com_cathode_pin, GPIO.LOW)
    
    # Set the segment pins to display the desired digit
    for i, val in enumerate(digits[digit]):
        GPIO.output(segments[i], val)
    
    # Wait for a short period of time to display the digit
    time.sleep(0.1)
    
    # Turn off all segment pins to clear the display
    GPIO.output(segments, GPIO.LOW)
    
    # Set the common anode/cathode pin to the opposite value to turn off the digit
    GPIO.output(com_anode_pin, GPIO.LOW)
    GPIO.output(com_cathode_pin, GPIO.HIGH)

# Display the number 1234 on the 7 segment display
display_digit('1')
display_digit('2')
display_digit('3')
display_digit('4')

# Clean up the GPIO pins before exiting the program
GPIO.cleanup()
