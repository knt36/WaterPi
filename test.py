import RPi.GPIO as GPIO
import time
from datetime import datetime

# BCM numbering, so GPIO2 is pin 3
PIN = 2

# Setup
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def pin_callback(channel):
    voltage = GPIO.input(channel)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # milliseconds precision
    print(f"[{timestamp}] Pin {channel} changed! New state: {'HIGH' if voltage else 'LOW'}")

# Detect both rising and falling edges
GPIO.add_event_detect(PIN, GPIO.BOTH, callback=pin_callback, bouncetime=50)

print("Monitoring voltage changes on GPIO2 (pin 3). Press Ctrl+C to exit.")
try:
    while True:
        time.sleep(1)  # Sleep to reduce CPU usage
except KeyboardInterrupt:
    print("\nExiting.")
finally:
    GPIO.cleanup()

