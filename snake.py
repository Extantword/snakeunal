from collections import deque
import random

GAME_CONTINUE = 0
APPLE_EATEN = -1
GAME_LOST = 1

matrix = [[0] * 13 for _ in range(13)]

def update_snake(snake, direction, apple = None):

    x, y = snake[-1]

    if(direction == 'W'): 
        new_head = (x, y + 1) # Agregar una nueva cabeza
    elif(direction == 'S'):
        new_head = (x, y - 1) # Agregar una nueva cabeza
    elif(direction == 'D'): 
        new_head = (x + 1, y) # Agregar una nueva cabeza
    elif(direction == 'A'):
        new_head = (x - 1, y) # Agregar una nueva cabeza

    new_x, new_y = new_head

   #3. La serpiente no se toca consigo misma
    if(matrix[new_x][new_y] == 1):
        return GAME_LOST #-1 signfica que se perdió el juego

    #.... SE VALIDAN LAS 3 CONDICIONES QUE DIJIMOS: 

    #1. La serpiente no se sale de la matriz
    if(not (0 <= new_x < 13 and 0 <= new_y < 13)):
        return GAME_LOST

    if(new_head != apple): #2. Si hay una manzana 
        snake.popleft() # Quitar la cola
        matrix[new_x][new_y] = 0
    

    snake.append(new_head) #Mover a la serpiente
    matrix[new_x][new_y] = 1 #Actualizar la matriz

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

    return random.randint(0, 12)

def start_game():

    snake = deque([(6, 8), (6, 7), (6, 6)]) #(2, 1)

    matrix[6][6] = 1
    matrix[7][6] = 1 #Iniciar la serpiente al principio
    matrix[8][6] = 1

    apple = (8, 2)
    matrix[2][8] = 2

    game_is_over = False
    apple_counter = 0

    while(not game_is_over):

        command = input()
        command = command.upper()
        

        if(command == 'W' or command == 'S' or command == 'A' or command == 'D'): #Validaciones de que se ingresó algo correcto

            status = update_snake(snake, command, apple)

            if(status == APPLE_EATEN):

                time = random_apple_generation()

                pass

            print(matrix)

            if(status == GAME_LOST):
                print('PERDISTE!')

            if(len(snake) >= 13 * 13):
                print('GANASTE!')
                break


"""FALTA LO SIGUIENTE:

-1. CUADRAR LA COSA DE LAS COORDENADAS O VER QUE HACER CON ESO (ESTÁN AL REVÉS)
1. LA COSA DE LOS 10 MOVIMIENTOS PARA PONER LA MANZANA 
2. VERIFICAR QUE EL JUEGO ES MINIMAMENTE FUNCIONAL
3. ACLARAR AL USUARIO COMO SE INGRESAN LOS INPUTS
4. NOTIFICAR QUE EL JUEGO ACABÓ (PREGUNTAR A JULIÁN LA ESPECIFICIDAD DE ESE MENSAJE)

PRÓXIMA REUNIÓN: LUNES A LAS 2?

"""