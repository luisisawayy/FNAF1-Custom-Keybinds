import pyautogui
import time
import keyboard

# All coordinates were calibrated with respect to a fullscreen 1920x1200 resolution. Adjust accordingly for different setups.
# Check out tracker.py for a real-time mouse position tracker to help calibrate coordinates for your setup.
PAN_LEFT_X = 10
PAN_RIGHT_X = 1910
CENTER_X, CENTER_Y = 960, 600

L_DOOR = (68, 418)
L_LIGHT = (68, 563)
R_DOOR = (1520, 435)
R_LIGHT = (1520, 574)
TABLET = (700, 885)
MUTE_PHONE = (105, 35)
HONK_FREDDY = (848, 298)

PAN_DELAY = 0.4  # buffer time for the in-game camera to finish swinging over

def fnaf_action(action_id):
    """Executes mouse movements for a given action in FNAF, based on input ID (key pressed)."""
        
    if action_id == 1:
        print("Action 1: Toggling Camera Tablet")
        pyautogui.moveTo(TABLET[0], TABLET[1])
        pyautogui.moveTo(706, 765) # custom coords to retrigger the tablet dropdown 
        
    elif action_id == 2:
        print("Action 2: Toggling Left Door")
        pyautogui.moveTo(PAN_LEFT_X, CENTER_Y)
        time.sleep(PAN_DELAY)
        pyautogui.click(L_DOOR[0], L_DOOR[1])
        
    elif action_id == 3:
        print("Action 3: Flashing Left Light (0.5s)")
        pyautogui.moveTo(PAN_LEFT_X, CENTER_Y)
        time.sleep(PAN_DELAY)
        pyautogui.click(L_LIGHT[0], L_LIGHT[1])
        time.sleep(0.5)
        pyautogui.click(L_LIGHT[0], L_LIGHT[1]) 
        
    elif action_id == 4:
        print("Action 4: Toggling Right Door")
        pyautogui.moveTo(PAN_RIGHT_X, CENTER_Y)
        time.sleep(PAN_DELAY)
        pyautogui.click(R_DOOR[0], R_DOOR[1])
        
    elif action_id == 5:
        print("Action 5: Flashing Right Light (0.5s)")
        pyautogui.moveTo(PAN_RIGHT_X, CENTER_Y)
        time.sleep(PAN_DELAY)
        pyautogui.click(R_LIGHT[0], R_LIGHT[1])
        time.sleep(0.5) 
        pyautogui.click(R_LIGHT[0], R_LIGHT[1])
        
    elif action_id == 6:
        print("Action 6: Muting Phone Guy")
        pyautogui.click(MUTE_PHONE[0], MUTE_PHONE[1])

    elif action_id == 7:
        print("Action 7: Honk Freddy's Nose")
        pyautogui.click(HONK_FREDDY[0], HONK_FREDDY[1]) # only works while looking fully left

# keyboard bindings for FNAF actions 1-7
keyboard.add_hotkey('1', lambda: fnaf_action(1))
keyboard.add_hotkey('2', lambda: fnaf_action(2))
keyboard.add_hotkey('3', lambda: fnaf_action(3))
keyboard.add_hotkey('4', lambda: fnaf_action(4))
keyboard.add_hotkey('5', lambda: fnaf_action(5))
keyboard.add_hotkey('6', lambda: fnaf_action(6))
keyboard.add_hotkey('7', lambda: fnaf_action(7))

print("""
=========================================
Keyboard Control Menu - Five Nights at Freddy's  
=========================================
[1] Toggle Camera Tablet
[2] Toggle Left Door
[3] Flash Left Light (0.5s)
[4] Toggle Right Door
[5] Flash Right Light (0.5s)
[6] Mute Phone Guy
[7] Honk Freddy's Nose (Look Left First!)
-----------------------------------------
Press keys 1-7 to perform actions
Press 'ESC' to exit
=========================================
""")
keyboard.wait('esc')