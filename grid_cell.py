import pygame
class GridCell(pygame.Rect):
    '''
    state = blank, yellow, green, grey.
    letter = A to Z
    '''
    def __init__(self, x, y, size, state = 'blank', letter = None):
        super().__init__(x, y, size, size)
        self.original_size = size
        self.state = state
        self.letter = letter

        #animation
        self.animating = False
        self.animation_progress = 0
        self.growth_factor = 1.2
        
    def set_state(self, new_state):
        """Update the cell's state"""
        valid_states = ['blank', 'yellow', 'green', 'grey', 'red']
        if new_state in valid_states:
            self.state = new_state
            if new_state != 'blank':
                self.animating = True
                self.animation_progress = 0

    def set_letter(self, char: str):
        """Sets letter to cell"""
        self.letter = char.upper() if char else None
    
    def reset(self):
        """Reset cell to blank state"""
        self.state = 'blank'
        self.letter = None
        self.animating = False
        self.animation_progress = 0

    def get_color(self):
        """Return color based on current state"""
        return {
            'blank': (58,58,60),    
            'grey': (58,58,60),    
            'yellow': (181,159,59),    
            'green': (83,141,78),
            'red': (100,0,0)     
        }.get(self.state, (255, 255, 255))

    def draw(self, screen):
        temp = self
        if self.animating:
            pulse_scale = 1 + (self.growth_factor - 1) * (1 - abs(self.animation_progress - 0.5) * 2)
            current_size = int(self.original_size * pulse_scale)
            offset = (self.original_size - current_size)//2
            temp = self.inflate(-offset,-offset)
            # self.width = current_size
            # self.height = current_size

            self.animation_progress += 0.1

            if self.animation_progress >= 1:
                self.animating = False
                

        if self.state == 'blank':
            # Draw the border
            pygame.draw.rect(screen, self.get_color(),temp, 2)
            return
        
        # Draw the cell rectangle
        pygame.draw.rect(screen, self.get_color(), temp)


        # Render the letter in the center of the cell
        if self.letter:  # Only draw if there's a letter
            font = pygame.font.SysFont('ClearSans', temp.width - 18)  # Adjust font size based on cell size
            text = font.render(self.letter.upper(), True, (255, 255, 255))  # White text
            text_rect = text.get_rect(center=(temp.x + temp.width // 2, temp.y + temp.width // 2))
            screen.blit(text, text_rect)

