import pyautogui
import random
from state import State
import time
    
fight_screen_bg_color = [52, 52, 52]
fight_screen_blank_xy = [533,733]
button_run_xy = [486, 755]

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
    #pyautogui.typewrite(path, 0.5)
    for key in path:
        hold_key(key, 0.2)
        print('pressed '+key+'\n')

def automove(h, l):
    move(path_circle_by_sizes(h, l))
    move(path_rand_by_sizes(h, l))

def hold_key(key, hold_time):
    start = time.time()
    pyautogui.keyDown(key)
    while time.time() - start < hold_time:
        pass
    pyautogui.keyUp(key)
    
#definition state machine
class MoveState(State):
    def on_event(self, event):
        if event == 'encounter':
            return EncounterState()

        return self
        
class EncounterState(State):
    def on_event(self, event):
        if event == 'pokemon_ok':
            return FightingState()
        if event == 'pokemon_ko':
            return MoveState()

        return self

class FightingState(State):
    def on_event(self, event):
        if event == 'encounter':
            return UnlockedState()

        return self

class WaitingState(State):
    def on_event(self, event):
        if event == 'encounter':
            return UnlockedState()

        return self

class LearningState(State):
    def on_event(self, event):
        if event == 'encounter':
            return UnlockedState()

        return self

states = ['move', 'encounter', 'check_pokemon', 'run']

current_state = MoveState()
#move(path_circle_by_sizes(4, 4))
#exit()

try:
    while True:
        #get mouse coordinates
        x, y = pyautogui.position()        
        #screenshot and get pixel color under the mouse cursor
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        
        if repr(current_state) == 'MoveState':
            
        
except KeyboardInterrupt:
    print('\nDone')
        


    
    