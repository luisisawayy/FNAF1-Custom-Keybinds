## Five Nights at Freddy's 1 Custom Keybinds
* `tracker.py` - When run, every 5 seconds, the terminal prints your X and Y coordinates with respect to your mouse position and display resolution. Used to calculate the exact coordinates of in-game actions (e.g., where exactly is the left door on the screen) that PyAutoGUI can use to perform the actions.
* `binds_logic.py` - Contains the logic for 7 different actions in FNAF, bound to the number keys 1-7. In-game actions are performed by PyAutoGUI upon pressing a designated number key.

Controls Menu:
* [1] Toggle Camera Tablet
* [2] Toggle Left Door
* [3] Flash Left Light (0.5s)
* [4] Toggle Right Door
* [5] Flash Right Light (0.5s)
* [6] Mute Phone Guy
* [7] Honk Freddy's Nose 

*To be implemented:*

Logic that defines a system to cycle through the cameras one the tablet is up


