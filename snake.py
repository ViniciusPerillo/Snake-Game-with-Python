from time import sleep
import keyboard

snake_map = []
snake_head_test = {
    'x': 1,
    'y': 1
}

direction = {
    'x': 0,
    'y': 0,
    'is_changed': False 
}

def frame():
    snake_head_test['x'] += direction['x']
    snake_head_test['y'] += direction['y']
    snake_map[snake_head_test['x']][snake_head_test['y']] = 'o '
    print(snake_map_str())
    sleep(1)
    direction['is_changed'] = False


def reset_snake_map():
    for i in range(0,31):
        matrix_line = []
        for j in range(0,31):
            if(i == 0 or j == 0 or i == 30 or j == 30 ):
                matrix_line.append('x ')
            else:            
                matrix_line.append('  ')
        snake_map.append(matrix_line)


def snake_map_str():
    map_str = ''
    for line in snake_map:
        for collumn in line:
            map_str += collumn
        map_str += '\n'
    return map_str


def arrow_up_event(evt):
    if(direction['x'] != 1 ):
        direction['y']= 0
        direction['x'] = -1
        direction['is_changed'] = True

def arrow_down_event(evt):
    if(direction['x'] != -1 ):
        direction['y']= 0
        direction['x'] = 1
        direction['is_changed'] = True

def arrow_left_event(evt):
    if(direction['y'] != 1 ):
        direction['y'] = -1
        direction['x']= 0
        direction['is_changed'] = True

def arrow_right_event(evt):
    if(direction['y'] != -1 ):
        direction['y'] = 1
        direction['x']= 0
        direction['is_changed'] = True


#Código principal
reset_snake_map()
keyboard.on_release_key('up', arrow_up_event)
keyboard.on_release_key('down', arrow_down_event)
keyboard.on_release_key('left', arrow_left_event)
keyboard.on_release_key('right', arrow_right_event)
while not keyboard.is_pressed('esc'):
    frame()
    
