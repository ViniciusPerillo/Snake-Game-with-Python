from time import sleep

snake_map = []


def run():
    create_snake_map()
    for c in range(0,10):
        frame()

def frame():
    print(snake_map_str())
    sleep(1)

def create_snake_map():
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

run()