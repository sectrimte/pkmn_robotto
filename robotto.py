import pyautogui
import random

fight_screen_bg_color = [52, 52, 52]
fight_screen_blank_xy = []
button_run_xy = []

def path_circle_by_sizes(height, length):
    path = ['right']*length + ['down']*height + ['left']*length + ['up']*height
    return path
    
def path_rand_by_sizes(height, length, current_position=[0, 0]):
    directions = ['right', 'left', 'down', 'up']
    delta_x = [1, -1, 0, 0]
    delta_y = [0, 0, 1, -1]
    path = []
    for i in range(100):
        next_step = random.randint(0, 3)
        if (0 <= current_position[0] + delta_x[next_step] < length) and (0 <= current_position[1] + delta_y[next_step] < height):
            path.append(directions[next_step])
            current_position[0] = current_position[0] + delta_x[next_step]
            current_position[1] = current_position[1] + delta_y[next_step]
    return path

def move(path):
    pyautogui.typewrite(path, 0.25)

move(path_circle_by_sizes(3, 3))
move(path_rand_by_sizes(3, 3))
    
try:
    while True:
        #get mouse coordinates
        x, y = pyautogui.position()
        
        #screenshot and get pixel color under the mouse cursor
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        
except KeyboardInterrupt:
    print('\nDone')
    


    
    