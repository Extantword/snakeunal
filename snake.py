from collections import deque
import random
import os

GAME_CONTINUE = 0
APPLE_EATEN = -1
GAME_LOST = 1
INVALID_MOVEMENT = 2

matrix = [[0] * 13 for _ in range(13)]

def print_matrix(matrix, snake):

    print('-'*15)

    for i, row in enumerate(matrix):
        
        str_ = "|"

        for j, char in enumerate(row):
            
            if((j, i) == snake[-1]):
                str_+= "░"
            elif(char == 0):
                str_ += " "
            elif(char == 1):
                str_ += "█"
            elif(char == 2):
                str_ += "●"

        str_ += "|"
        
        print(str_)

    print('-'*15)

def update_snake(snake, direction, apple = None):

    x, y = snake[-1]

    if(direction == 'W'): 
        new_head = (x, y - 1) # Agregar una nueva cabeza
    elif(direction == 'S'):
        new_head = (x, y + 1) # Agregar una nueva cabeza
    elif(direction == 'D'): 
        new_head = (x + 1, y) # Agregar una nueva cabeza
    elif(direction == 'A'):
        new_head = (x - 1, y) # Agregar una nueva cabeza

    new_x, new_y = new_head

    #.... SE VALIDAN LAS 4 CONDICIONES QUE DIJIMOS: 

    if((new_x, new_y) == snake[-2]):
        return INVALID_MOVEMENT

    #La serpiente no se sale de la matriz
    if(not (0 <= new_x < 13 and 0 <= new_y < 13)):
        return GAME_LOST
    
       # print('new_y:',new_y, 'new_x',new_x)

    x_tail, y_tail = snake[0]
    #La serpiente no se toca consigo misma
    if(matrix[new_y][new_x] == 1 and (new_x != x_tail or new_y != y_tail)):
        return GAME_LOST #-1 significa que se perdió el juego

    if(new_head != apple): #2. Si no hay una manzana 
        snake.popleft() # Quitar la cola
        matrix[y_tail][x_tail] = 0

    snake.append(new_head) #Mover a la serpiente
    matrix[new_y][new_x] = 1 #Actualizar la matriz

    if(new_head == apple):
        return APPLE_EATEN #1 Significa que si se comió la manzana

    return GAME_CONTINUE #0 significa que el juego continua

def add_apple():

    possible_y = []

    for i in range(13):

        if 0 in matrix[i]:
            possible_y.append(i)
    
    y_random = random.choice(possible_y)
    possible_x = []

    for j in range(13):

        if matrix[y_random][j] == 0:

            possible_x.append(j)

    x_random = random.choice(possible_x)
    apple = (x_random, y_random)

    return apple



def random_apple_generation():

    return random.randint(1, 10)

def start_game():

    snake = deque([(6, 8), (6, 7), (6, 6)]) #(2, 1)

    matrix[6][6] = 1
    matrix[7][6] = 1 #Iniciar la serpiente al principio
    matrix[8][6] = 1

    apple = add_apple()
    x_apple, y_apple = apple
    matrix[y_apple][x_apple] = 2

    game_is_over = False
    apple_counter = 0

    print_matrix(matrix, snake)
    time = 0

    while(not game_is_over):

        command = input()
        command = command.upper()

        if(command == 'W' or command == 'S' or command == 'A' or command == 'D'): #Validaciones de que se ingresó algo correcto
            os.system('cls')
            print('¡Bienvenido a SnakeUNAL! \nIngresa un solo caracter (W, A, S, D) para mover a la serpiente')

            status = update_snake(snake, command, apple)

            if(status == INVALID_MOVEMENT):
                print('¡La serpiente no puede devolverse sobre si misma!')
                continue

            if(apple is None):
                apple_counter += 1

            if(status == APPLE_EATEN):
                apple = None
                apple_counter = 0
                time = random_apple_generation()
                #print('#MOV:', time)

            elif(apple_counter == time and apple is None):
                apple = add_apple()
                x_apple, y_apple = apple

                if(apple in snake):
                    print('ERROR!')

                matrix[y_apple][x_apple] = 2
                apple_counter = 0
            
            print_matrix(matrix, snake)

            if(status == GAME_LOST):
                print('¡PERDISTE!')
                break

            if(len(snake) >= 13 * 13):
                print('¡GANASTE!')
                break
        else:
            print('Haz ingresado una tecla no válida!')

    
os.system('cls')    
print('¡Bienvenido a SnakeUNAL! \nIngresa un solo caracter (W, A, S, D) para mover a la serpiente')
start_game()