import pygame
import time
import math

from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# global background_color, background_color_board
background_color = (240, 230, 140)
background_color_board = (255, 0, 255)
screen.fill(background_color)

SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

img = pygame.image.load('wood.png')
img_width, img_height = img.get_size()

# While loop will continue work until runnning become False
running = True

# number of rectangles on baord
number_rectangles = 9

# Array for empty & vacant positions
space_area = ''
board_array = [1, 2, 3,
               5, space_area, 8,
               6, 7, 4]

temp_array = board_array[:]

final_array = []
for num in range(number_rectangles - 1):
    final_array.append(num + 1)
final_array.append(space_area)
# print(final_array)

number_font = pygame.font.Font(None, 150)
small_number_font = pygame.font.Font(None, 70)

# divide screen width by 4 to use the middle area for the board
img_wid = SCREEN_WIDTH / 4
small_rectangle_dimension = 70

# X, Y for numbers on the game board
number_on_board_x1 = img_wid + 50
number_on_board_x2 = img_wid + 200

number_on_board_y1 = 180
number_on_board_y2 = number_on_board_y1 + 150

i, j = 0, 0
numbers_big_board_xy = []
for num in range(number_rectangles):
    numbers_big_board_xy.append((number_on_board_x1, number_on_board_y1))
    if i < math.sqrt(number_rectangles) - 1:
        i += 1
        j = 0
        number_on_board_x1 = number_on_board_x2
        number_on_board_x2 += 150
    else:
        i, j = 0, 0
        number_on_board_y1 = number_on_board_y2
        number_on_board_y2 = number_on_board_y1 + 150
        number_on_board_x1 = img_wid + 50
        number_on_board_x2 = img_wid + 200

# X, Y for small board rectangles, START
x1_small_board = img_wid * 3 + 20
x2_small_board = x1_small_board + small_rectangle_dimension

y1_small_board = 10
y2_small_board = y1_small_board + small_rectangle_dimension

i, j = 0, 0
small_rectangle_xy = []
for num in range(number_rectangles):
    small_rectangle_xy.append((x1_small_board, y1_small_board, small_rectangle_dimension, small_rectangle_dimension))
    if i < round(math.sqrt(number_rectangles)) - 1:
        j = 0
        i += 1
        x1_small_board = x2_small_board
        x2_small_board += small_rectangle_dimension
    else:
        y1_small_board = y2_small_board
        y2_small_board += small_rectangle_dimension
        j, i = 0, 0
        x1_small_board = img_wid * 3 + 20
        x2_small_board = x1_small_board + small_rectangle_dimension
# X, Y for small board rectangles, END

# X, Y for numbers on the small board
number_small_board_x1 = img_wid * 3 + 20
number_small_board_x2 = number_small_board_x1 + small_rectangle_dimension

number_small_board_y1 = 10
number_small_board_y2 = number_small_board_y1 + small_rectangle_dimension

i, j = 0, 0
numbers_small_board_xy = []
for num in range(number_rectangles):
    numbers_small_board_xy.append((number_small_board_x1, number_small_board_y1))
    if i < math.sqrt(number_rectangles) - 1:
        i += 1
        j = 0
        number_small_board_x1 = number_small_board_x2
        number_small_board_x2 += small_rectangle_dimension
    else:
        i, j = 0, 0
        number_small_board_y1 = number_small_board_y2
        number_small_board_y2 = number_small_board_y1 + small_rectangle_dimension
        number_small_board_x1 = img_wid * 3 + 20
        number_small_board_x2 = number_small_board_x1 + small_rectangle_dimension
# X, Y for numbers on the small board


rectangle_color = (0, 0, 0)
# global rectangle_dimension, rectangle_x, rectangle_y, rectangle_thickness
big_rectangle_dimension = 150
rectangle_x = img_wid
rectangle_y = 150
rectangle_thickness = 10

player_name = "Player Name: "
player_font = pygame.font.Font(None, 50)

quit_game = "Quit"

# X,Y for each big rectangle
x1 = img_wid
x2 = x1 + big_rectangle_dimension

y1 = rectangle_y
y2 = y1 + big_rectangle_dimension

number_sqrt = round(math.sqrt(number_rectangles))
big_rectangle_xy = []
i, j = 0, 0
for num in range(number_rectangles):
    big_rectangle_xy.append((x1, y1, big_rectangle_dimension, big_rectangle_dimension))
    if i < number_sqrt - 1:
        x1 = x2
        x2 += big_rectangle_dimension
        j = 0
        i += 1

    else:
        i = 0
        y1 = y2
        y2 += big_rectangle_dimension
        j += 1
        x1 = img_wid
        x2 = x1 + big_rectangle_dimension


# X,Y for each big rectangle


# move number to empty position based on mouse click by user action
def move_to_rectangle(**move_para):
    global numbers_big_board_xy, background_color, board_array, space_area

    # Swap old number and put space in the old location
    board_array[move_para['board_new_location']] = board_array[move_para['board_old_location']]
    board_array[move_para['board_old_location']] = space_area


# move number to empty position based on mouse click by user action


# function to be called after mouse position matching in big_rectangle_dict
def big_rectangle_func(**rect_para):
    global board_array, background_color, space_area, number_font
    click = pygame.mouse.get_pressed()

    if click[0] == 1:

        if board_array[rect_para['new_location_xy1']] == space_area:
            print('after click1 ', rect_para['new_location_xy1'], rect_para['new_location_xy2'])
            move_to_rectangle(board_old_location=rect_para['old_location_xy'],
                              board_new_location=rect_para['new_location_xy1'])
        elif board_array[rect_para['new_location_xy2']] == space_area:
            print('after click2 ', rect_para['new_location_xy1'], rect_para['new_location_xy2'],
                  board_array[rect_para['new_location_xy2']])
            move_to_rectangle(board_old_location=rect_para['old_location_xy'],
                              board_new_location=rect_para['new_location_xy2'])


# function to be called after mouse position matching in big_rectangle_dict
func_dict = [
    big_rectangle_func,
    big_rectangle_func,
    big_rectangle_func,
    big_rectangle_func,
    big_rectangle_func,
    big_rectangle_func,
    big_rectangle_func,
    big_rectangle_func,
    big_rectangle_func]

big_rectangle_dict = {k: v for k, v in zip(big_rectangle_xy, func_dict)}


# print('len=', (big_rectangle_dict))


# Function to display exit msg when the user click quit or press ESC
def close_program(**close_para):
    while True:
        pygame.draw.rect(screen, (255, 0, 0),
                         (close_para['rect_x_pos'], close_para['rect_y_pos'], close_para['rect_width'],
                          close_para['rect_height']), close_para['rect_thickness'])
        close_font = pygame.font.Font(None, 50)
        closing = close_font.render(close_para['text'], True, close_para['font_color'])
        screen.blit(closing, (close_para['screen_x'], close_para['screen_y']))
        pygame.display.flip()
        for event_key in pygame.event.get():
            if event_key.type == KEYDOWN:
                if event_key.key in (K_ESCAPE, K_y):
                    return False
                elif event_key.key in (K_SPACE, K_n):
                    return True


# Function to display exit msg when the user click quit or press ESC

# Function to get player name from the user
def get_player_name():
    name = ''
    running1 = True
    global background_color
    close = "Please enter your name"
    close_font = pygame.font.Font(None, 50)
    closing = close_font.render(close, True, (255, 0, 0))
    screen.blit(closing, (150, 250))
    pygame.display.flip()

    while running1:
        for event_key in pygame.event.get():
            if event_key.type == KEYDOWN:
                if event_key.key == K_ESCAPE:
                    running1 = False
                elif event_key.unicode.isalpha() or event_key.unicode.isdigit() or event_key.key == K_SPACE:
                    name += event_key.unicode
                elif event_key.key == K_BACKSPACE:
                    name = name[:-1]
                    screen.fill(background_color)
                elif event_key.key in (K_KP_ENTER, K_RETURN):
                    return name
        closing1 = close_font.render(name, True, (255, 0, 0))
        screen.blit(closing, (150, 250))
        screen.blit(closing1, (150, 300))
        pygame.display.flip()


# Function to get player name from the user


player1_name = get_player_name()
screen.fill(background_color)


# Function to display Quit button
def button(**button_para):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    global background_color, quit_game, SCREEN_WIDTH, SCREEN_HEIGHT

    running1 = True
    if button_para['rect_width'] + button_para['rect_x'] > cursor[0] > button_para['rect_x'] and \
            button_para['rect_height'] + button_para['rect_y'] > cursor[1] > button_para['rect_y']:
        quit_render = button_para['object_font'].render(quit_game, True, background_color)
        screen.blit(quit_render, (button_para['blit_x'], button_para['blit_y']))
        if click[0] == 1:
            while running1:
                background_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                if close_program(text="Do you want to exit? (Yes, No)", rect_x_pos=140, rect_y_pos=240,
                                 rect_width=510,
                                 rect_height=50,
                                 font_color=(0, 0, 0),
                                 screen_x=150,
                                 screen_y=250,
                                 rect_thickness=0):
                    # retrieve old display after removing dialog
                    screen.blit(background_surface, (0, 0))
                    screen.fill(background_color)
                    running1 = False
                else:
                    pygame.quit()


# Function to display Quit button


# move number to empty position based on COMPUTER action
def move_to_rectangle_AI(**move_para):
    global numbers_big_board_xy, background_color, board_array, space_area, temp_array

    # screen.blit(move_para['player_render2'], (array_numbers_xy[move_para['numbers_xy']]))
    # Retrieve the old screen surface
    # screen.fill(background_color)
    # pygame.display.flip()
    board_array[move_para['board_new_location']] = board_array[move_para['board_old_location']]
    board_array[move_para['board_old_location']] = space_area
    reset_temp_array()


# move number to empty position based on COMPUTER action


# Check which number clicked and call Move_to_rectangle to move it based on mouse click
def move_number(**move_param):
    # cursor to save mouse cursor coordinates and Click to show which mouse button pressed
    cursor = pygame.mouse.get_pos()
    # click = pygame.mouse.get_pressed()

    global number_font, big_rectangle_dimension, background_color_board, background_color, numbers_big_board_xy
    global board_array, space_area, big_rectangle_dict

    rect_x1, rect_y1, rect_x2, rect_y2 = move_param['mouse_pos']
    if rect_x2 + rect_x1 > cursor[0] > rect_x1 and rect_y2 + rect_y1 > cursor[1] > rect_y1:
        player_render1 = number_font.render(str(move_param['board_number']), True, background_color_board)
        screen.blit(player_render1, move_param['blit_xy'])

        # Call dictionary, mouse pos as key, moveing numbers as a value
        big_rectangle_dict[move_param['mouse_pos']](old_location_xy=0,
                                                    new_location_xy1=1,
                                                    new_location_xy2=3)
        big_rectangle_dict[move_param['mouse_pos']](old_location_xy=1,
                                                    new_location_xy1=0,
                                                    new_location_xy2=2,
                                                    new_location_xy3=4)
        big_rectangle_dict[move_param['mouse_pos']](old_location_xy=2,
                                                    new_location_xy1=1,
                                                    new_location_xy2=5)
        big_rectangle_dict[move_param['mouse_pos']](old_location_xy=3,
                                                    new_location_xy1=0,
                                                    new_location_xy2=4,
                                                    new_location_xy3=6)
        big_rectangle_dict[move_param['mouse_pos']](old_location_xy=4,
                                                    new_location_xy1=1,
                                                    new_location_xy2=5,
                                                    new_location_xy3=7,
                                                    new_location_xy4=3)
        big_rectangle_dict[move_param['mouse_pos']](old_location_xy=5,
                                                    new_location_xy1=8,
                                                    new_location_xy2=4,
                                                    new_location_xy3=2)
        big_rectangle_dict[move_param['mouse_pos']](old_location_xy=6,
                                                    new_location_xy1=3,
                                                    new_location_xy2=7)
        big_rectangle_dict[move_param['mouse_pos']](old_location_xy=7,
                                                    new_location_xy1=6,
                                                    new_location_xy2=4,
                                                    new_location_xy3=8)
        big_rectangle_dict[move_param['mouse_pos']](old_location_xy=8,
                                                    new_location_xy1=7,
                                                    new_location_xy2=5)

        '''if move_param['rectangle_no'] == 1:
                # player_render2 = number_font.render(str(board_array[0]), True, background_color)
                if board_array[1] == space_area:
                    move_to_rectangle(board_old_location=0, board_new_location=1)
                elif board_array[3] == space_area:
                    move_to_rectangle(board_old_location=0, board_new_location=3)

            elif move_param['rectangle_no'] == 2:
                if board_array[0] == space_area:
                    move_to_rectangle(board_old_location=1, board_new_location=0)

                elif board_array[2] == space_area:
                    move_to_rectangle(board_old_location=1, board_new_location=2)

                elif board_array[4] == space_area:
                    move_to_rectangle(board_old_location=1, board_new_location=4)

            elif move_param['rectangle_no'] == 3:
                player_render2 = number_font.render(str(board_array[2]), True, background_color)

                if board_array[1] == space_area:
                    move_to_rectangle(board_old_location=2, board_new_location=1, player_render2=player_render2,
                                      numbers_xy=1)

                elif board_array[5] == space_area:
                    move_to_rectangle(board_old_location=2, board_new_location=5, player_render2=player_render2,
                                      numbers_xy=5)

            elif move_param['rectangle_no'] == 4:
                player_render2 = number_font.render(str(board_array[3]), True, background_color)

                if board_array[0] == space_area:
                    move_to_rectangle(board_old_location=3, board_new_location=0, player_render2=player_render2,
                                      numbers_xy=0)
                elif board_array[4] == space_area:
                    move_to_rectangle(board_old_location=3, board_new_location=4, player_render2=player_render2,
                                      numbers_xy=4)
                elif board_array[6] == space_area:
                    move_to_rectangle(board_old_location=3, board_new_location=6, player_render2=player_render2,
                                      numbers_xy=6)

            elif move_param['rectangle_no'] == 5:
                player_render2 = number_font.render(str(board_array[4]), True, background_color)
                if board_array[1] == space_area:
                    move_to_rectangle(board_old_location=4, board_new_location=1, player_render2=player_render2,
                                      numbers_xy=1)
                elif board_array[5] == space_area:
                    move_to_rectangle(board_old_location=4, board_new_location=5, player_render2=player_render2,
                                      numbers_xy=5)
                elif board_array[7] == space_area:
                    move_to_rectangle(board_old_location=4, board_new_location=7, player_render2=player_render2,
                                      numbers_xy=7)
                elif board_array[3] == space_area:
                    move_to_rectangle(board_old_location=4, board_new_location=3, player_render2=player_render2,
                                      numbers_xy=3)

            elif move_param['rectangle_no'] == 6:
                player_render2 = number_font.render(str(board_array[5]), True, background_color)
                if board_array[2] == space_area:
                    move_to_rectangle(board_old_location=5, board_new_location=2, player_render2=player_render2,
                                      numbers_xy=2)
                elif board_array[4] == space_area:
                    move_to_rectangle(board_old_location=5, board_new_location=4, player_render2=player_render2,
                                      numbers_xy=4)
                elif board_array[8] == space_area:
                    move_to_rectangle(board_old_location=5, board_new_location=8, player_render2=player_render2,
                                      numbers_xy=8)

            elif move_param['rectangle_no'] == 7:
                player_render2 = number_font.render(str(board_array[6]), True, background_color)
                if board_array[3] == space_area:
                    move_to_rectangle(board_old_location=6, board_new_location=3, player_render2=player_render2,
                                      numbers_xy=3)
                elif board_array[7] == space_area:
                    move_to_rectangle(board_old_location=6, board_new_location=7, player_render2=player_render2,
                                      numbers_xy=7)

            elif move_param['rectangle_no'] == 8:
                player_render2 = number_font.render(str(board_array[7]), True, background_color)
                if board_array[8] == space_area:
                    move_to_rectangle(board_old_location=7, board_new_location=8, player_render2=player_render2,
                                      numbers_xy=8)
                elif board_array[4] == space_area:
                    move_to_rectangle(board_old_location=7, board_new_location=4, player_render2=player_render2,
                                      numbers_xy=4)
                elif board_array[6] == space_area:
                    move_to_rectangle(board_old_location=7, board_new_location=6, player_render2=player_render2,
                                      numbers_xy=6)

            elif move_param['rectangle_no'] == 9:
                player_render2 = number_font.render(str(board_array[8]), True, background_color)
                if board_array[5] == space_area:
                    move_to_rectangle(board_old_location=8, board_new_location=5, player_render2=player_render2,
                                      numbers_xy=5)
                elif board_array[7] == space_area:
                    move_to_rectangle(board_old_location=8, board_new_location=7, player_render2=player_render2,
                                      numbers_xy=7)
        '''
        # pygame.display.flip()
        # screen.fill(background_color)


# Check which number clicked and call Move_to_rectangle to move it based on mouse click


# Computer will move numbers based on empty rectangle
def move_ai():
    global number_font, big_rectangle_dimension, background_color_board, background_color, numbers_big_board_xy, space_area
    global board_array, temp_array

    if board_array[0] == '':
        check_array(1)

    elif board_array[1] == '':
        check_array(2)

    elif board_array[2] == '':
        check_array(3)

    elif board_array[3] == '':
        check_array(4)

    elif board_array[4] == '':
        check_array(5)

    elif board_array[5] == '':
        check_array(6)

    elif board_array[6] == '':
        check_array(7)

    elif board_array[7] == '':
        check_array(8)

    elif board_array[8] == '':
        check_array(9)

    pygame.display.flip()
    screen.fill(background_color)


# Computer will move numbers based on empty rectangle


# Function to Draw rectangles as per the given parameters
def draw_rect(**rect):
    global screen, rectangle_color, rectangle_thickness
    rect_x1, rect_y1, rect_x2, rect_y2 = rect['rectangle_xy']
    # print('rect=', rect_x1, rect_y1, rect_x2, rect_y2)
    pygame.draw.rect(screen,
                     rectangle_color,
                     (rect_x1, rect_y1,
                      rect_x2,
                      rect_y2),
                     rectangle_thickness)


# Function to Draw rectangles as per the given parameters

# Count how many numbers not arranged in the correct position
def count_numbers():
    global temp_array, board_array
    count = 0
    j = 1

    for row in temp_array:
        if row != j:
            count += 1
        j += 1

    return count


# Count how many numbers not arranged in the correct position


# Reset temp array by copying board array to temp array after each move
def reset_temp_array():
    global temp_array, board_array

    temp_array = board_array[:]


# Reset temp array by copying board array to temp array after each move


# Swap numbers to check and evaluate the next move  based on the smallest number of movement
def check_array(rect_no):
    global temp_array, board_array
    count = []

    if rect_no in (1, 3, 7, 9):
        if rect_no == 1:
            new_location = 0
            old_location1 = 1
            old_location2 = 3

        elif rect_no == 3:
            new_location = 2
            old_location1 = 5
            old_location2 = 1

        elif rect_no == 7:
            new_location = 6
            old_location1 = 3
            old_location2 = 7

        elif rect_no == 9:
            new_location = 8
            old_location1 = 7
            old_location2 = 5

        # Temp array is a copy of board array used to check the which number has less steps to be moved
        temp_array[new_location], temp_array[old_location1] = temp_array[old_location1], \
                                                              temp_array[new_location]
        count.append(count_numbers())
        # Copy original array to temp array
        reset_temp_array()

        temp_array[new_location], \
        temp_array[old_location2] = temp_array[old_location2], temp_array[new_location]

        count.append(count_numbers())
        reset_temp_array()

        if count[0] < count[1]:
            move_to_rectangle_AI(board_old_location=old_location1, board_new_location=new_location)
        else:
            move_to_rectangle_AI(board_old_location=old_location2, board_new_location=new_location)

    elif rect_no in (2, 4, 6, 8):
        old_location_2 = 4
        if rect_no == 2:
            new_location = 1
            old_location_1 = 2
            old_location_3 = 0
        elif rect_no == 4:
            new_location = 3
            old_location_1 = 0
            old_location_3 = 6
        elif rect_no == 6:
            new_location = 5
            old_location_1 = 8
            old_location_3 = 2
        elif rect_no == 8:
            new_location = 7
            old_location_1 = 6
            old_location_3 = 8

        # Temp array is a copy of board array used to check the which number has less steps to be moved
        temp_array[new_location], temp_array[old_location_1] = temp_array[old_location_1], \
                                                               temp_array[new_location]
        count.append(count_numbers())
        reset_temp_array()

        temp_array[new_location], temp_array[old_location_2] = temp_array[old_location_2], \
                                                               temp_array[new_location]
        count.append(count_numbers())
        reset_temp_array()

        temp_array[new_location], temp_array[old_location_3] = temp_array[old_location_3], \
                                                               temp_array[new_location]
        count.append(count_numbers())
        reset_temp_array()

        if count[0] < count[1] and count[0] < count[2]:  # or count[1] == 0:
            move_to_rectangle_AI(board_old_location=old_location_1, board_new_location=new_location)
        elif count[1] < count[0] and count[1] < count[2]:
            move_to_rectangle_AI(board_old_location=old_location_2, board_new_location=new_location)
        else:
            move_to_rectangle_AI(board_old_location=old_location_3, board_new_location=new_location)

    elif rect_no == 5:
        new_location = 4
        old_location_1 = 5
        old_location_2 = 7
        old_location_3 = 3
        old_location_4 = 1

        temp_array[new_location], temp_array[old_location_1] = temp_array[old_location_1], \
                                                               temp_array[new_location]
        count.append(count_numbers())
        reset_temp_array()
        temp_array[new_location], temp_array[old_location_2] = temp_array[old_location_2], \
                                                               temp_array[new_location]
        count.append(count_numbers())
        reset_temp_array()
        temp_array[new_location], temp_array[old_location_3] = temp_array[old_location_3], \
                                                               temp_array[new_location]
        count.append(count_numbers())
        reset_temp_array()

        temp_array[new_location], temp_array[old_location_4] = temp_array[old_location_4], \
                                                               temp_array[new_location]
        count.append(count_numbers())
        reset_temp_array()

        if count[0] < count[1] and count[0] < count[2] and count[0] < count[3]:  # or count[1] == 0:
            move_to_rectangle_AI(board_old_location=old_location_1, board_new_location=new_location)
        elif count[1] < count[0] and count[1] < count[2] and count[1] < count[3]:
            move_to_rectangle_AI(board_old_location=old_location_2, board_new_location=new_location)
        elif count[2] < count[0] and count[2] < count[1] and count[2] < count[3]:
            move_to_rectangle_AI(board_old_location=old_location_3, board_new_location=new_location)
        else:
            move_to_rectangle_AI(board_old_location=old_location_4, board_new_location=new_location)
# Swap numbers to check and evaluate the next move  based on the smallest number of movement


# List for goal board numbers
goal_board_numbers = []

# main program loop start here
while running:
    # List for game board numbers
    game_board_numbers = []

    #pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                # Copy current display to background before called close dialog
                background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                if close_program(text="Do you want to exit? (Yes, No)", rect_x_pos=140, rect_y_pos=240, rect_width=510,
                                 rect_height=50, font_color=(0, 0, 0), screen_x=150, screen_y=250, rect_thickness=0):
                    running = True
                    # retrieve old display after removing dialog
                    screen.blit(background, (0, 0))
                    screen.fill(background_color)
                else:
                    running = False

    # Wood sign board for player name
    screen.blit(img, (img_wid, 0))
    player_render = player_font.render(player_name, True, (0, 0, 0))
    player_name_render = player_font.render(player1_name, True, (0, 0, 0))
    screen.blit(player_render, (img_wid + 10, 80))
    screen.blit(player_name_render, (img_wid + 240, 80))

    # Wood sign board for Quit
    screen.blit(img, ((img_wid * 2.5), 0))

    # Dislay Quit on the wood board
    player_render = player_font.render(quit_game, True, (0, 0, 0))
    screen.blit(player_render, (img_wid * 2.6, 80))

    # Display rectangles on the goal board
    for num in range(number_rectangles):
        draw_rect(rectangle_xy=small_rectangle_xy[num])

    # Numbers on the goal board
    for final in final_array:
        goal_board_numbers.append(small_number_font.render(str(final), True, (0, 0, 0)))

    # blit number as per array_number position
    for i, num in enumerate(numbers_small_board_xy):
        screen.blit(goal_board_numbers[i], num)

    # Display big rectangles for the numbers grid
    for num in range(number_rectangles):
        draw_rect(rectangle_xy=big_rectangle_xy[num])

    # Numbers on the big board
    for i, final in enumerate(board_array):
        # print('final',board_array)
        game_board_numbers.append(number_font.render(str(final), True, (0, 0, 0)))

    # blit numbers on the big board
    for num, final in enumerate(numbers_big_board_xy):
        screen.blit(game_board_numbers[num], final)

    # Function for Quit button only
    button(blit_x=img_wid * 2.6, blit_y=80, rect_x=img_wid * 2.5, rect_y=0, rect_width=img_width,
           rect_height=img_height, object_font=player_font)

    # Function move_ai to move number to empty location (COMPUTER ACTION)
    move_ai()

    # Function move_number to move number to empty location (USER ACTION)
    '''for i in range(number_rectangles):
        move_number(rectangle_no=i + 1,
                    mouse_pos=big_rectangle_xy[i],
                    blit_xy=numbers_big_board_xy[i],
                    board_number=board_array[i])
'''
    # Check if the user arranged the puzzle as per the original arrangement
    if board_array == final_array:
        final_msg = player_font.render("You won", True, (0, 0, 0))
        screen.blit(final_msg, (200, 200))

    time.sleep(1)
    pygame.display.flip()
# main program loop end here
