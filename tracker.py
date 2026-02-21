import pyautogui
import time
import keyboard
import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion

# MQTT Configuration - send output to phone via MQTT
# Done to better see terminal output in real time as my mouse hovered over the In-Game Actions
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "fnaf/cv/coords/luisg-99" 

client = mqtt.Client(CallbackAPIVersion.VERSION2)
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start() 

counter = 1

try:
    while True:
        if keyboard.is_pressed('esc'):
            print("\nTracker stopped.")
            break
            
        time.sleep(5)
        
        # get x and y coordinates of mouse position
        x, y = pyautogui.position()
        message = f"Log #{counter} | X: {x}, Y: {y}"
        
        # publish output to phone and terminal
        client.publish(MQTT_TOPIC, message)
        print(f"Coordinates - {message}") 
        
        counter += 1
        
except KeyboardInterrupt:
    print("\nTracker stopped.")
finally:
    client.loop_stop()
    client.disconnect()