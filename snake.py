from time import sleep
from os import system, name
from random import randint
import keyboard

#Variables
snake_map = []
snake_body = []
food = {}
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
    move_snake()
    eat_food()
    system('cls' if name == 'nt' else 'clear')
    print(snake_map_str())
    print('{:^42}'.format('Segure ESC para sair'))
    sleep(0.2)
    


def create_snake_map():
    for i in range(21):
        matrix_column = []
        for j in range(21):            
                matrix_column.append('')
        snake_map.append(matrix_column)


def clean_snake_map():
    for j in range(21):
        for i in range(21):
            if(i == 0 or j == 0 or i == 20 or j == 20 ):
                snake_map[j][i] = 'x '
            else:
                snake_map[j][i] = '  '

def snake_map_str():
    map_str = ''
    for line in snake_map:
        for column in line:
            map_str += column
        map_str += '\n'
    return map_str


def reset_snake_body():
    for c in range(11,8,-1):
        snake_body.append({
            'x': c,
            'y': 15
        })
        write_snake_body()


def spawn_snake_body(x, y):
    snake_body.append({
        'x': x,
        'y': y
    })

def write_snake_body():
    for sb in snake_body:
        snake_map[sb['y']][sb['x']] = 'o '


def erase_snake_body():
    for y in range(21):
        for x in range(21):
            snake_map[y][x] = snake_map[y][x].replace('o', ' ')


def move_snake():
    erase_snake_body()
    for index in range(len(snake_body)-1,-1,-1):
        if(index == 0):
            snake_body[index]['x'] += direction['x']
            snake_body[index]['y'] += direction['y']
        else:
            snake_body[index] = snake_body[index-1].copy()
    write_snake_body()
    direction['is_changed'] = False


def spawn_food():
    food['x'] = randint(1,19)
    food['y'] = randint(1,19)
    for sb in snake_body:
        if(sb['x'] == food['x'] and sb['y'] == food['y']):
            spawn_food()
    snake_map[food['y']][food['x']] = 'f '

def eat_food():
    if snake_body[0] == food:
        spawn_snake_body(food['x'], food['y'])
        spawn_food()

#Código principal
constructor()
spawn_food()
print(snake_map_str())
print('{:^42}'.format('Pressione qualquer seta para começar'))
while not direction['is_changed']:
    pass
while not keyboard.is_pressed('esc'):
    frame()
    
