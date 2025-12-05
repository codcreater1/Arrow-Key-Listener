# arrow_key_listener.py

from pynput import keyboard

def on_press(key):
    try:
        if key.char:
            print(f"You pressed the character: {key.char}")
    except AttributeError:
        
        if key == keyboard.Key.up:
            print("You pressed the UP arrow!")
        elif key == keyboard.Key.down:
            print("You pressed the DOWN arrow!")
        elif key == keyboard.Key.left:
            print("You pressed the LEFT arrow!")
        elif key == keyboard.Key.right:
            print("You pressed the RIGHT arrow!")
        elif key == keyboard.Key.esc:
            print("Exiting program...")
            return False  

print("Press arrow keys (ESC to quit)...")

with keyboard.Listessner(on_press=on_press) as listener:
    listener.join()
