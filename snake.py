from collections import deque
import random
import os

GAME_CONTINUE = 0
APPLE_EATEN = -1
GAME_LOST = 1
INVALID_MOVEMENT = 2

matrix = [[0] * 13 for _ in range(13)]

def print_matrix(matrix):

    print('-'*15)

    for row in matrix:
        
        str_ = "|"

        for char in row:

            if(char == 0):
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
    
    #La serpiente no se toca consigo misma
    if(matrix[new_y][new_x] == 1):
        return GAME_LOST #-1 signfica que se perdió el juego

    if(new_head != apple): #2. Si hay una manzana 
        x_tail, y_tail = snake[0]
        snake.popleft() # Quitar la cola
        matrix[y_tail][x_tail] = 0

       # print('new_y:',new_y, 'new_x',new_x)

    snake.append(new_head) #Mover a la serpiente
    matrix[new_y][new_x] = 1 #Actualizar la matriz

    if(new_head == apple):
        return APPLE_EATEN #1 Signfica que si se comió la manzana

    return GAME_CONTINUE #0 significa que el juego continua

def add_apple():

    possible_x = []

    for i in range(13):

        if 0 in matrix[i]:
            possible_x.append(i)
    
    x_random = random.choice(possible_x)
    possible_y = []

    for j in range(13):

        if matrix[x_random][j] == 0:

            possible_y.append(j)

    y_random = random.choice(possible_y)
    apple = (x_random, y_random)
    return apple

def random_apple_generation():

    return random.randint(1, 10)

def start_game():

    snake = deque([(6, 8), (6, 7), (6, 6)]) #(2, 1)

    matrix[6][6] = 1
    matrix[7][6] = 1 #Iniciar la serpiente al principio
    matrix[8][6] = 1

    apple = (8, 2)
    matrix[2][8] = 2

    game_is_over = False
    apple_counter = 0

    print_matrix(matrix)
    time = 0

    while(not game_is_over):

        command = input()
        command = command.upper()

        if(command == 'W' or command == 'S' or command == 'A' or command == 'D'): #Validaciones de que se ingresó algo correcto

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
                matrix[y_apple][x_apple] = 2
                apple_counter = 0
            
            print_matrix(matrix)

            if(status == GAME_LOST):
                print('¡PERDISTE!')
                break

            if(len(snake) >= 13 * 13):
                print('¡GANASTE!')
                break
        else:
            print('Haz ingresado una tecla no válida!')

        
print('¡Bienvenido a SnakeUNAL! \nIngresa un solo caracter (W, A, S, D) para mover a la serpiente')
start_game()

"""FALTA LO SIGUIENTE:

-1. CUADRAR LA COSA DE LAS COORDENADAS O VER QUE HACER CON ESO (ESTÁN AL REVÉS)

1. LA COSA DE LOS 10 MOVIMIENTOS PARA PONER LA MANZANA (LISTO!!)

2. VERIFICAR QUE EL JUEGO ES MINIMAMENTE FUNCIONAL (LISTO!!)

3. ACLARAR AL USUARIO COMO SE INGRESAN LOS INPUTS
4. NOTIFICAR QUE EL JUEGO ACABÓ (PREGUNTAR A JULIÁN LA ESPECIFICIDAD DE ESE MENSAJE)

PRÓXIMA REUNIÓN: LUNES A LAS 2?
"""