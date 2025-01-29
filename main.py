import pygame
from grid_cell import GridCell
from word_guesser import WordGuess
from display_message import MessageDisplay

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Wordle")

# secret_word = 'CHORE'
secret = WordGuess(randomize=True, length=5)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (18, 18, 18)

#font
FONT = pygame.font.SysFont('ClearSans', 80)  # Adjust size as needed


# Constants for the grid
CELL_SIZE = 55
CELL_PADDING = 8
GRID_ROWS = 6
GRID_COLS = len(secret.word)
GRID_START_X = (screen_width - (GRID_COLS * (CELL_SIZE + CELL_PADDING)) + CELL_PADDING) // 2
GRID_START_Y = (screen_height - (GRID_ROWS * (CELL_SIZE + CELL_PADDING)) + CELL_PADDING) // 2 + 50
grid = [[None] * GRID_COLS for i in range(GRID_ROWS)]
for row in range(GRID_ROWS):
    for col in range(GRID_COLS):
        x = GRID_START_X + col * (CELL_SIZE + CELL_PADDING)
        y = GRID_START_Y + row * (CELL_SIZE + CELL_PADDING)
        grid[row][col] = GridCell(x, y, CELL_SIZE)

# Draw function
def draw_grid(screen, message):
    screen.fill(GREY)
    text = FONT.render("Wordle", True, WHITE)  # White color
    message.draw(screen)
    text_rect = text.get_rect(center=(screen.get_width() // 2, 50))  # Centered horizontally, 50px from top
    screen.blit(text, text_rect)
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            grid[row][col].draw(screen)



message_display = MessageDisplay(display_time=3)
#cursor
curr_y, curr_x = 0, 0
played_words = []

# Main game loop
running = True
game_end = False
guessing = ''
while running:

    pygame.time.Clock().tick(60)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if game_end:
                continue
            
            if event.key >= 97 and event.key <= 122:
                pressed = chr(event.key)
                #move cursor
                if curr_x == 0 and curr_y == 0 and grid[curr_y][0].state == 'blank':
                    guessing += pressed
                    pass
                elif curr_x < GRID_COLS - 1:
                    guessing += pressed
                    curr_x += 1

                if grid[curr_y][curr_x].state == 'blank':
                    cell = grid[curr_y][curr_x]
                    cell.set_state('grey')
                    cell.set_letter(pressed)
                   
            elif event.key == pygame.K_BACKSPACE:
                guessing = guessing[:-1]
                cell = grid[curr_y][curr_x]
                cell.set_state('blank')
                cell.set_letter(None)

                if curr_x == -1:
                    pass
                else:
                    curr_x -= 1
                
            elif event.key == pygame.K_RETURN:

                #########################
                # if(guessing=="negro"):
                #     game_end = True
                #     ##############
                #     negro = 'negro'
                #     for row in range(curr_y,GRID_ROWS):
                #         for col in range(GRID_COLS):
                #             if col < 5:
                #                 grid[row][col].set_letter(negro[col])
                #             else:
                #                 grid[row][col].set_letter('!')
                #             grid[row][col].set_state('red')

                    ###############

                if len(guessing) == GRID_COLS:
                    result, isCorrect, isValid = secret.guess(guessing)

                    if not isValid: # skip invalid
                        message_display.set_message('Invalid word')
                        continue
                    if guessing in played_words:
                        message_display.set_message('You already played that Bruh')
                        continue

                    played_words.append(guessing)
                    guessing = ''

                    i = 0
                    wait_time = 10
                    curr_frame_count = 0
                    while i < GRID_COLS:
                        pygame.time.Clock().tick(60)
                        curr_frame_count += 1
                        if curr_frame_count >= wait_time:
                            grid[curr_y][i].set_state(result[i])
                            curr_frame_count = 0
                            i += 1
                        draw_grid(screen, message_display)
                        pygame.display.flip()
                    
                    if curr_y < GRID_ROWS:
                        curr_y += 1
                        curr_x = -1

                    if curr_y == GRID_ROWS or isCorrect:
                        game_end = True
                        ##############
                        # negro = 'negro'
                        # for row in range(curr_y,GRID_ROWS):
                        #     for col in range(GRID_COLS):
                        #         if col < 5:
                        #             grid[row][col].set_letter(negro[col])
                        #         else:
                        #             grid[row][col].set_letter('!')
                        #         grid[row][col].set_state('red')
                        ############
                        if not isCorrect:
                            message_display.set_message(f'The word was {secret.word}!')
                        else:
                            message_display.set_message('Congratulations!')
                else:
                    if (len(guessing) == 0):
                        message_display.set_message('Write something first ohmagawd')
                    else:
                        message_display.set_message('Cant you see the blank squares?')

                # if(curr_y==GRID_ROWS):
                #     message_display.set_message("Give up NEGRO!!")

                    
    # Draw the grid
    draw_grid(screen, message_display)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()