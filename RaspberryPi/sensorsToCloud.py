import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import RPi.GPIO as GPIO

# Set up Firebase credentials and initialize Firestore
cred = credentials.Certificate("path/to/serviceAccountKey.json")  # Replace with your service account key file
firebase_admin.initialize_app(cred)
db = firestore.client()

# Pin definitions for temperature and smoke sensors
TEMP_PINS = [4, 5, 6, 7, 8, 9]  # Replace with the GPIO pins connected to the temperature sensors
SMOKE_PINS = [10, 11, 12, 13, 14, 15]  # Replace with the GPIO pins connected to the smoke sensors

# Function to read temperature from sensor
def read_temperature(pin):
    # Placeholder code to read temperature from the sensor connected to the given pin
    # Replace this code with the actual implementation for your temperature sensor
    # Return the temperature value read from the sensor
    temperature = 0  # Replace with the actual code to read temperature
    return temperature

# Function to read smoke value from sensor
def read_smoke(pin):
    # Placeholder code to read smoke value from the sensor connected to the given pin
    # Replace this code with the actual implementation for your smoke sensor
    # Return the smoke value read from the sensor
    smoke = 0  # Replace with the actual code to read smoke value
    return smoke

# Function to send data to Firestore
def send_data_to_firestore(node, temperature, smoke):
    doc_ref = db.collection(u'sensor_data').document(node)
    doc_ref.set({
        u'temperature': temperature,
        u'smoke': smoke,
        u'timestamp': firestore.SERVER_TIMESTAMP
    })

# Main loop
try:
    GPIO.setmode(GPIO.BCM)
    nodes = ['node1', 'node2', 'node3', 'node4', 'node5', 'node6']

    while True:
        for i in range(len(nodes)):
            temperature = read_temperature(TEMP_PINS[i])
            smoke = read_smoke(SMOKE_PINS[i])

            if temperature is not None and smoke is not None:
                send_data_to_firestore(nodes[i], temperature, smoke)
                print(f"Data sent to Firestore - Node: {nodes[i]}, Temperature: {temperature}, Smoke: {smoke}")
            else:
                print(f"Failed to read sensor data for Node: {nodes[i]}")

        time.sleep(5)  # Delay between readings
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()  # Clean up GPIO pins when the program exits




