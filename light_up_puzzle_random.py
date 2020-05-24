import random
import numpy as np
import matplotlib.pyplot as plt
from random import randrange
import logging

puzzle_line_size = 7
puzzle_column_size = 7
puzzle_table = []
forbidden_positions = []
possible_solutions_for_ones = []
possible_solutions_for_twos = []
possible_solutions_for_threes = []
possible_solutions_for_fours = []
remaining_position_after_init = []

# cria um novo jogo de forma aleatória
def create_populated_table_positions():
    dark_number_percentage_max = 10
    dark_empty_percentage_max = 15
    one_hundred_percent = 100
    max_dark_number = 5
    fill_with =  "      "
    for i in range(puzzle_line_size) :
        line = []
        for j in range(puzzle_column_size):
            number_pecentage = random.randrange(0, one_hundred_percent, 1)
            if (number_pecentage < dark_number_percentage_max):
                fill_with = "dark_" +  str(random.randrange(0, max_dark_number, 1))
            elif (number_pecentage < dark_empty_percentage_max):
                fill_with = "dark  "
            else:
                fill_with =  "      "
            line.append(fill_with)
        puzzle_table.append(line)

# imprime um jogo na tela
def print_puzzle_table():
    fig = plt.figure(dpi=200)
    ax = fig.add_subplot(1,1,1)

    table = ax.table(cellText=puzzle_table, loc='center')
    table.set_fontsize(20)
    table.scale(1,1)
    ax.axis('off')
    plt.show()

# verifica se posição está na tabela
def is_at_table_puzzle(i,j):
    is_at_table_puzzle = True
    if ((i >= puzzle_line_size) or (i < 0) or (j >= puzzle_line_size) or (j < 0)):
       is_at_table_puzzle = False
    return is_at_table_puzzle

# verifica quais posições estão, inicialmente, proibidas
def create_initial_forbidden_positions():
    for i in range(puzzle_line_size) :
        for j in range(puzzle_column_size):
            if (puzzle_table[i][j] == "dark  " or 
                puzzle_table[i][j] == "dark_0" or
                puzzle_table[i][j] == "dark_1" or
                puzzle_table[i][j] == "dark_2" or
                puzzle_table[i][j] == "dark_3" or
                puzzle_table[i][j] == "dark_4"):
                forbidden_positions.append([i,j])

            if (puzzle_table[i][j] == "dark_0"):
                possible_forbidden_position_i = i-1
                possible_forbidden_position_j = j
                if (is_at_table_puzzle(possible_forbidden_position_i, possible_forbidden_position_j)):
                    forbidden_positions.append([possible_forbidden_position_i, possible_forbidden_position_j])

                possible_forbidden_position_i = i+1
                possible_forbidden_position_j = j
                if (is_at_table_puzzle(possible_forbidden_position_i, possible_forbidden_position_j)):
                    forbidden_positions.append([possible_forbidden_position_i, possible_forbidden_position_j])

                
                possible_forbidden_position_i = i
                possible_forbidden_position_j = j - 1
                if (is_at_table_puzzle(possible_forbidden_position_i, possible_forbidden_position_j)):
                    forbidden_positions.append([possible_forbidden_position_i, possible_forbidden_position_j])

                
                possible_forbidden_position_i = i
                possible_forbidden_position_j = j + 1
                if (is_at_table_puzzle(possible_forbidden_position_i, possible_forbidden_position_j)):
                    forbidden_positions.append([possible_forbidden_position_i, possible_forbidden_position_j])

# cria possiveis soluções para as posições do jogo
def create_possible_solutions():
    for i in range(puzzle_line_size) :
        for j in range(puzzle_column_size):
            if (puzzle_table[i][j] == "dark_1"):
                create_possible_solutions_for_one(i,j)
            if (puzzle_table[i][j] == "dark_2"):
                create_possible_solutions_for_two(i,j)
            if (puzzle_table[i][j] == "dark_3"):
                create_possible_solutions_for_three(i,j)
            if ((puzzle_table[i][j] == "dark_4")):
                create_possible_solutions_for_four(i,j)

# cria possiveis soluções para a posição um
def create_possible_solutions_for_one(i,j):
    solutions_one = []
    if (is_at_table_puzzle(i-1,j) and (not forbidden_positions.__contains__([i-1,j]))):
        solutions_one.append([i-1,j])
    if (is_at_table_puzzle(i+1,j) and (not forbidden_positions.__contains__([i+1,j]))):
        solutions_one.append([i+1,j])
    if (is_at_table_puzzle(i,j-1) and (not forbidden_positions.__contains__([i,j-1]))):
        solutions_one.append([i,j-1])
    if (is_at_table_puzzle(i,j+1) and (not forbidden_positions.__contains__([i,j+1]))):
        solutions_one.append([i,j+1])
    possible_solutions_for_ones.append(solutions_one)
        
# cria possiveis soluções para a posição dois
def create_possible_solutions_for_two(i,j):
    solutions_two = []
    if (is_at_table_puzzle(i-1,j) 
    and is_at_table_puzzle(i,j-1)
    and (not forbidden_positions.__contains__([i-1,j]))
    and (not forbidden_positions.__contains__([i,j-1]))):
        solutions_two.append([[i-1,j],[i,j-1]])

    if (is_at_table_puzzle(i-1,j) 
    and is_at_table_puzzle(i+1,j) 
    and (not forbidden_positions.__contains__([i-1,j]))
    and (not forbidden_positions.__contains__([i+1,j]))):
        solutions_two.append([[i-1,j],[i+1,j]])

    if (is_at_table_puzzle(i-1,j) 
    and is_at_table_puzzle(i,j+1) 
    and (not forbidden_positions.__contains__([i-1,j]))
    and (not forbidden_positions.__contains__([i,j+1]))):
        solutions_two.append([[i-1,j],[i,j+1]])

    if (is_at_table_puzzle(i,j-1) 
    and is_at_table_puzzle(i+1,j) 
    and (not forbidden_positions.__contains__([i,j-1]))
    and (not forbidden_positions.__contains__([i+1,j]))):
        solutions_two.append([[i,j-1],[i+1,j]])
    
    if (is_at_table_puzzle(i,j-1) 
    and is_at_table_puzzle(i,j+1) 
    and (not forbidden_positions.__contains__([i,j-1]))
    and (not forbidden_positions.__contains__([i,j+1]))):
        solutions_two.append([[i,j-1],[i,j+1]])
                    
    if (is_at_table_puzzle(i+1,j) 
    and is_at_table_puzzle(i,j+1) 
    and (not forbidden_positions.__contains__([i+1,j]))
    and (not forbidden_positions.__contains__([i,j+1]))):
        solutions_two.append([[i+1,j],[i,j+1]])
                
    possible_solutions_for_twos.append(solutions_two)

# cria possiveis soluções para a posição tres
def create_possible_solutions_for_three(i,j):
    solutions_three = []
    if (is_at_table_puzzle(i-1,j) 
        and is_at_table_puzzle(i,j-1) 
        and is_at_table_puzzle(i,j+1)
        and (not forbidden_positions.__contains__([i-1,j]))
        and (not forbidden_positions.__contains__([i,j-1]))
        and (not forbidden_positions.__contains__([i,j+1]))):
        solutions_three.append([[i-1,j],[i,j-1],[i,j+1]])

    if (is_at_table_puzzle(i-1,j) 
        and is_at_table_puzzle(i+1,j) 
        and is_at_table_puzzle(i,j+1)
        and (not forbidden_positions.__contains__([i-1,j]))
        and (not forbidden_positions.__contains__([i+1,j]))
        and (not forbidden_positions.__contains__([i,j+1]))):
        solutions_three.append([[i-1,j],[i+1,j],[i,j+1]])
    
    if (is_at_table_puzzle(i,j-1) 
        and is_at_table_puzzle(i+1,j) 
        and is_at_table_puzzle(i,j+1)
        and (not forbidden_positions.__contains__([i,j-1]))
        and (not forbidden_positions.__contains__([i+1,j]))
        and (not forbidden_positions.__contains__([i,j+1]))):
        solutions_three.append([[i,j-1],[i+1,j],[i,j+1]])

    if (is_at_table_puzzle(i-1,j) 
        and is_at_table_puzzle(i,j-1) 
        and is_at_table_puzzle(i+1,j)
        and (not forbidden_positions.__contains__([i-1,j]))
        and (not forbidden_positions.__contains__([i,j-1]))
        and (not forbidden_positions.__contains__([i+1,j]))):
        solutions_three.append([[i-1,j],[i,j-1],[i+1,j]])
    possible_solutions_for_threes.append(solutions_three)

# cria possiveis soluções para a posição quatro   
def create_possible_solutions_for_four(i,j):
    solutions_four = []
    if (is_at_table_puzzle(i-1,j) 
        and is_at_table_puzzle(i+1,j) 
        and is_at_table_puzzle(i,j+1) 
        and is_at_table_puzzle(i,j-1)
        and (not forbidden_positions.__contains__([i-1,j]))
        and (not forbidden_positions.__contains__([i+1,j]))
        and (not forbidden_positions.__contains__([i,j+1]))
        and (not forbidden_positions.__contains__([i,j-1]))):
        solutions_four.append([[i-1,j],[i+1,j],[i,j+1],[i,j-1]])
    possible_solutions_for_fours.append(solutions_four)

# atualiza jogo com luzes
def update_puzzle_light(position_lamp_x, position_lamp_y):
    forbidden_positions.append([position_lamp_x,position_lamp_y])
    i = position_lamp_x
    j = position_lamp_y + 1
    dark_list = ["dark  ", "dark_0", "dark_1", "dark_2", "dark_3", "dark_4"]
    if(is_at_table_puzzle(i,j)):
        while (j < puzzle_column_size) and (puzzle_table[i][j] not in dark_list):
            puzzle_table[i][j] = "light "
            forbidden_positions.append([i,j])
            j= j + 1
    
    i = position_lamp_x
    j = position_lamp_y - 1
    if(is_at_table_puzzle(i,j)):
        while (j >= 0) and (puzzle_table[i][j] not in dark_list):
            puzzle_table[i][j] = "light "
            forbidden_positions.append([i,j])
            j= j - 1
    
    i = position_lamp_x + 1
    j = position_lamp_y
    dark_list = ["dark  ", "dark_0", "dark_1", "dark_2", "dark_3", "dark_4"]
    if(is_at_table_puzzle(i,j)):
        while (i < puzzle_column_size) and (puzzle_table[i][j] not in dark_list):
            puzzle_table[i][j] = "light "
            forbidden_positions.append([i,j])
            i= i + 1
    
    i = position_lamp_x - 1
    j = position_lamp_y
    if(is_at_table_puzzle(i,j)):
        while (i >= 0) and (puzzle_table[i][j] not in dark_list):
            puzzle_table[i][j] = "light "
            forbidden_positions.append([i,j])
            i= i - 1

# inicializa jogo de forma aleatória com possíveis posições
def init_puzzle_generation():

    is_initial_solution_valid = True

    for i in range(len(possible_solutions_for_fours)):
        j = random.randrange(0, len(possible_solutions_for_fours[i]), 1)
        solution = possible_solutions_for_fours[i][j]
        if(forbidden_positions.__contains__([solution[0][0],solution[0][1]]) or
          (forbidden_positions.__contains__([solution[1][0],solution[1][1]])) or
          (forbidden_positions.__contains__([solution[2][0],solution[2][1]])) or
          (forbidden_positions.__contains__([solution[3][0],solution[3][1]]))):
            is_initial_solution_valid = False
            return is_initial_solution_valid
        else:
            puzzle_table[solution[0][0]][solution[0][1]] = "lamp  "
            puzzle_table[solution[1][0]][solution[1][1]] = "lamp  "
            puzzle_table[solution[2][0]][solution[2][1]] = "lamp  "
            puzzle_table[solution[3][0]][solution[3][1]] = "lamp  "
            update_puzzle_light(solution[0][0], solution[0][1])
            update_puzzle_light(solution[1][0], solution[1][1])
            update_puzzle_light(solution[2][0], solution[2][1])
            update_puzzle_light(solution[3][0], solution[3][1])

    for i in range(len(possible_solutions_for_threes)):
        j = random.randrange(0, len(possible_solutions_for_threes[i]), 1)
        solution = possible_solutions_for_threes[i][j]
        if(forbidden_positions.__contains__([solution[0][0],solution[0][1]]) or
          (forbidden_positions.__contains__([solution[1][0],solution[1][1]])) or
          (forbidden_positions.__contains__([solution[2][0],solution[2][1]]))):
            is_initial_solution_valid = False
            return is_initial_solution_valid
        else:
            puzzle_table[solution[0][0]][solution[0][1]] = "lamp  "
            puzzle_table[solution[1][0]][solution[1][1]] = "lamp  "
            puzzle_table[solution[2][0]][solution[2][1]] = "lamp  "
            update_puzzle_light(solution[0][0], solution[0][1])
            update_puzzle_light(solution[1][0], solution[1][1])
            update_puzzle_light(solution[2][0], solution[2][1])


    for i in range(len(possible_solutions_for_twos)):
        j = random.randrange(0, len(possible_solutions_for_twos[i]), 1)
        solution = possible_solutions_for_twos[i][j]
        if(forbidden_positions.__contains__([solution[0][0],solution[0][1]]) or
          (forbidden_positions.__contains__([solution[1][0],solution[1][1]]))):
            is_initial_solution_valid = False
            return is_initial_solution_valid
        else:
            puzzle_table[solution[0][0]][solution[0][1]] = "lamp  "
            puzzle_table[solution[1][0]][solution[1][1]] = "lamp  "
            update_puzzle_light(solution[0][0], solution[0][1])
            update_puzzle_light(solution[1][0], solution[1][1])
    
    for i in range(len(possible_solutions_for_ones)):
        j = random.randrange(0, len(possible_solutions_for_ones[i]), 1)
        solution = possible_solutions_for_ones[i][j]

        if(forbidden_positions.__contains__([solution[0],solution[1]])):
            is_initial_solution_valid = False
            return is_initial_solution_valid
        else:
            puzzle_table[solution[0]][solution[1]] = "lamp  "
            update_puzzle_light(solution[0],solution[1])

    return is_initial_solution_valid

# retorna o numero de combinações de soluções possíveis
def init_generations_combinations():
    init_generations_combinations = 1

    for i in range(len(possible_solutions_for_ones)):
        init_generations_combinations = init_generations_combinations*len(possible_solutions_for_ones[i])
    for i in range(len(possible_solutions_for_twos)):
        init_generations_combinations = init_generations_combinations*len(possible_solutions_for_twos[i])
    for i in range(len(possible_solutions_for_threes)):
        init_generations_combinations = init_generations_combinations*len(possible_solutions_for_threes[i])
    for i in range(len(possible_solutions_for_fours)):
        init_generations_combinations = init_generations_combinations*len(possible_solutions_for_fours[i])
    
    return init_generations_combinations

# inicializa jogo
def init_puzzle():
    global puzzle_table
    global forbidden_positions
    global possible_solutions_for_ones
    global possible_solutions_for_twos
    global possible_solutions_for_threes
    global possible_solutions_for_fours
    global remaining_position_after_init
    puzzle_table = []
    forbidden_positions = []
    possible_solutions_for_ones = []
    possible_solutions_for_twos = []
    possible_solutions_for_threes = []
    possible_solutions_for_fours = []
    remaining_position_after_init = []
    
    create_populated_table_positions()
    
    create_initial_forbidden_positions()
    
    create_possible_solutions()

# retorna as posições depois da inicialização
def remaining_position_after_init_function():
    for i in range(puzzle_line_size):
        for j in range(puzzle_column_size):
            if(puzzle_table[i][j] == "      "):
                remaining_position_after_init.append([i,j])

# verifica se o jogo foi resolvido
def is_game_solved():
    is_game_solved = True
    for i in range(puzzle_line_size):
        for j in range(puzzle_column_size):
            if((puzzle_table[i][j] != "dark  ") and
              (puzzle_table[i][j] != "dark_0") and
              (puzzle_table[i][j] != "dark_1") and
              (puzzle_table[i][j] != "dark_2") and
              (puzzle_table[i][j] != "dark_3") and
              (puzzle_table[i][j] != "dark_4") and
              (puzzle_table[i][j] != "lamp  ") and
              (puzzle_table[i][j] != "light ")):
              is_game_solved = False
            if((puzzle_table[i][j] == "dark_1") and (count_lamps_around_position(i,j) != 1)):
                is_game_solved = False
            if((puzzle_table[i][j] == "dark_2") and (count_lamps_around_position(i,j) != 2)):
                is_game_solved = False
            if((puzzle_table[i][j] == "dark_3") and (count_lamps_around_position(i,j) != 3)):
                is_game_solved = False

    return is_game_solved

# conta o numero de lampadas em volta de uma posição
def count_lamps_around_position(i,j):
    count_lamps = 0

    possible_position_i = i
    possible_position_j = j+1
    if (is_at_table_puzzle(possible_position_i,possible_position_j)):
        if(puzzle_table[possible_position_i][possible_position_j] == "lamp  "):
            count_lamps = count_lamps + 1

    possible_position_i = i
    possible_position_j = j-1
    if (is_at_table_puzzle(possible_position_i,possible_position_j)):
        if(puzzle_table[possible_position_i][possible_position_j] == "lamp  "):
            count_lamps = count_lamps + 1

    possible_position_i = i+1
    possible_position_j = j
    if (is_at_table_puzzle(possible_position_i,possible_position_j)):
        if(puzzle_table[possible_position_i][possible_position_j] == "lamp  "):
            count_lamps = count_lamps + 1

    possible_position_i = i-1
    possible_position_j = j
    if (is_at_table_puzzle(possible_position_i,possible_position_j)):
        if(puzzle_table[possible_position_i][possible_position_j] == "lamp  "):
            count_lamps = count_lamps + 1
    return count_lamps

# limpa posições do jogo
def init_puzzle_clean():
    for i in range(puzzle_line_size):
        for j in range(puzzle_column_size):
            if(puzzle_table[i][j] == "lamp  "):
                puzzle_table[i][j] = "      "
            if(puzzle_table[i][j] == "light "):
                puzzle_table[i][j] = "      "

# programa principal - tenta resoler um jogo especifico
logging.basicConfig(filename='seven_dimension_ten_mil_test.log', filemode='a', level=logging.INFO)

# inicializa o puzzle e tenta montar uma geração inicial
init_puzzle()
initial_generation_count = 0
init_generations_combinations = init_generations_combinations()
while (initial_generation_count < init_generations_combinations):
    init_puzzle_clean()
    if (init_puzzle_generation()):
        break
    initial_generation_count = initial_generation_count + 1
    
if (initial_generation_count < init_generations_combinations):
    print("Iterations to generate initial generation: " + str(initial_generation_count))
    logging.info("Iterations to generate initial generation: " + str(initial_generation_count))
    remaining_position_after_init_function()
    remainings_positions_tries = 50*len(remaining_position_after_init)
    remainings_positions_count = 0
else:
    print("It is not possible generate initial generation in " + str(initial_generation_count) + " iterations")
    logging.info("It is not possible generate initial generation in " + str(initial_generation_count) + " iterations")
    
    remainings_positions_tries = 0
    remainings_positions_count = 1

# tenta resolver o puzzle definitivamente
while (remainings_positions_count < remainings_positions_tries):    
    for i in range(len(remaining_position_after_init)):
        probability_lamp = randrange(100)
        if (probability_lamp < 80):
            puzzle_table[remaining_position_after_init[i][0]][remaining_position_after_init[i][1]] = "lamp  "
            update_puzzle_light(remaining_position_after_init[i][0], remaining_position_after_init[i][1])
    if (is_game_solved()):
        break
    remainings_positions_count = remainings_positions_count + 1
    
if (remainings_positions_count < remainings_positions_tries):
    print("SUCCESS: Iterations to solve the puzzle: " + str(remainings_positions_count))
    print("")
    logging.info("SUCCESS: Iterations to solve the puzzle: " + str(remainings_positions_count))
else:
    print("FAIL: It is not possible solve the puzzle with " + str(remainings_positions_count) + " iterations")
    print("")
    logging.info("FAIL: It is not possible solve the puzzle with " + str(remainings_positions_count) + " iterations")
   