from time import sleep
from os import system, name
import keyboard

#Variables
snake_map = []
snake_body = []

direction = {
    'x': 0,
    'y': 0,
    'is_changed': False 
}

#Listeners 
def arrow_up_event(evt):
    if(direction['y'] != 1 and not direction['is_changed']):
        direction['x'] = 0
        direction['y'] = -1
        direction['is_changed'] = True

def arrow_down_event(evt):
    if(direction['y'] != -1 and not direction['is_changed']):
        direction['x'] = 0
        direction['y'] = 1
        direction['is_changed'] = True

def arrow_left_event(evt):
    if(direction['x'] != 1 and not direction['is_changed']):
        direction['x'] = -1
        direction['y'] = 0
        direction['is_changed'] = True

def arrow_right_event(evt):
    if(direction['x'] != -1 and not direction['is_changed']):
        direction['x'] = 1
        direction['y'] = 0
        direction['is_changed'] = True


#Functions
def constructor():
    create_snake_map()
    reset_snake_body()
    keyboard.on_release_key('up', arrow_up_event)
    keyboard.on_release_key('down', arrow_down_event)
    keyboard.on_release_key('left', arrow_left_event)
    keyboard.on_release_key('right', arrow_right_event)


def frame():
    system('cls' if name == 'nt' else 'clear')
    clear_snake_map()
    move_snake()
    print(snake_map_str())
    print('{:^62}'.format('Segure ESC para sair'))
    sleep(0.5)
    direction['is_changed'] = False


def create_snake_map():
    for i in range(0,31):
        matrix_column = []
        for j in range(0,31):
            if(i == 0 or j == 0 or i == 30 or j == 30 ):
                matrix_column.append('x ')
            else:            
                matrix_column.append('  ')
        snake_map.append(matrix_column)


def clear_snake_map():
    for y, column in enumerate(snake_map):
        for x, slot in enumerate(column):
            if( y == 0 or x == 0 or y == 30 or x == 30 ):
                pass
            else:
                snake_map[y][x] = '  '

def snake_map_str():
    map_str = ''
    for line in snake_map:
        for collumn in line:
            map_str += collumn
        map_str += '\n'
    return map_str


def reset_snake_body():
    for c in range(17,14,-1):
        snake_body.append({
            'x': c,
            'y': 15
        })
        write_snake_body()


def write_snake_body():
    for sb in snake_body:
        snake_map[sb['y']][sb['x']] = 'o '


def move_snake():
    for index in range(len(snake_body)-1,-1,-1):
        if(index == 0):
            snake_body[index]['x'] += direction['x']
            snake_body[index]['y'] += direction['y']
        else:
            snake_body[index] = snake_body[index-1].copy()
    write_snake_body()


#Código principal
constructor()
print(snake_map_str())
print('{:^62}'.format('Pressione qualquer seta para começar'))
while not direction['is_changed']:
    pass
while not keyboard.is_pressed('esc'):
    frame()
    
