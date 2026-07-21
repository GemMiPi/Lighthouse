from machine import Pin, PWM
import time

# Create PWM Object
led = PWM(Pin(26), freq=1000)

""" Trying something new

while True:
    # Gradually increase brightness
    for duty_cycle in range(0, 1024, 6):
        led.duty(duty_cycle)
        time.sleep(0.01)

    for duty_cycle in range(1023, -1, -6):
        led.duty(duty_cycle)
        time.sleep(0.01)
"""
while True:
    # flash comes in on led at 0.4 seconds
    # Jumps by 25 every 10ms ~41 steps
    for duty_cycle in range(0, 1024, 25):
        led.duty(duty_cycle)
        time.sleep(0.01)

    for duty_cycle in range(1023, -1, -25):
        led.duty(duty_cycle)
        time.sleep(0.01)

    # Ensure LED is fully off after sweep
    led.duty(0)

    # Darkness (waiting for rotation)
    # Adjust this value to make rotation faster
    # or slower
    time.sleep(4.0)