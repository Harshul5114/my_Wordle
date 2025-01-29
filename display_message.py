import pygame
import time  # To track time for message visibility

class MessageDisplay:
    def __init__(self, font_size=40, color=(255, 255, 255), display_time=2):
        # Set up font, color, and default display time
        self.font = pygame.font.Font(None, font_size)  # Default font
        self.color = color
        self.message = ""  # No message by default
        self.visible = False  # Message is invisible by default
        self.display_time = display_time  # Duration for which message will be displayed (in seconds)
        self.time_triggered = None  # Time when message was triggered
    
    def set_message(self, message):
        """Set the message to display and record the time."""
        self.message = message
        self.visible = True  # Make the message visible
        self.time_triggered = time.time()  # Store the current time when the message is triggered
    
    def hide(self):
        """Hide the message."""
        self.visible = False
    
    def draw(self, screen):
        """Draw the message if it's visible, and handle the display duration."""
        if self.visible:
            # Check if the message display time has elapsed
            if time.time() - self.time_triggered >= self.display_time:
                self.hide()  # Hide the message if the duration has passed
            
            # Render the message text
            text = self.font.render(self.message, True, self.color)  # Render the message
            text_rect = text.get_rect(center=(screen.get_width() // 2, 120))  # Centered on screen, adjust Y
            screen.blit(text, text_rect)