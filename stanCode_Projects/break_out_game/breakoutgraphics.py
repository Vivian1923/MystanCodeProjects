"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        self.ball_radius = ball_radius
        self.b_width = brick_width
        self.b_height = brick_height
        self.b_rows = brick_rows
        self.b_cols = brick_cols
        self.b_spacing = brick_spacing
        self.b_offset = brick_offset
        self.p_width = paddle_width
        self.p_height = paddle_height
        self.p_offset = paddle_offset
        self.__dx = 0
        self.__dy = 0
        self.door_is_close = False
        self.v_is_fixed = False
        self.count_bricks = 0

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, (window_width-paddle_width)/2, window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(width=ball_radius*2, height=ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, (window_width-ball_radius*2)/2, (window_height-ball_radius*2)/2)

        # Default initial velocity for the ball

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.start_game)

        # Draw bricks
        for i in range(int(brick_rows)):
            for j in range(int(brick_cols)):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                if j <= 1:
                    self.bricks.color = 'red'
                    self.bricks.fill_color = 'red'
                elif 1 < j <= 3:
                    self.bricks.color = 'orange'
                    self.bricks.fill_color = 'orange'
                elif 3 < j <= 5:
                    self.bricks.color = 'yellow'
                    self.bricks.fill_color = 'yellow'
                elif 5 < j <= 7:
                    self.bricks.color = 'green'
                    self.bricks.fill_color = 'green'
                elif 7 < j <= 9:
                    self.bricks.color = 'blue'
                    self.bricks.fill_color = 'blue'
                self.window.add(self.bricks, i * (brick_width + brick_spacing),
                                brick_offset + j * (brick_height + brick_spacing))
                self.count_bricks += 1

    def move_paddle(self, mouse):
        self.paddle.x = mouse.x - (self.p_width / 2)
        if mouse.x < (self.p_width / 2):
            self.window.add(self.paddle, 0, self.window.height-self.p_offset)
        elif mouse.x > self.window.width-(self.p_width / 2):
            self.window.add(self.paddle, self.window.width-self.p_width, self.window.height-self.p_offset)
        else:
            self.window.add(self.paddle)

    def start_game(self, mouse):
        if not self.door_is_close:
            self.door_is_close = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self):
        self.__dx *= -1

    def set_dy(self):
        self.__dy *= -1

    def put_new_ball(self):
        self.window.add(self.ball, (self.window.width - self.b_width) / 2, (self.window.height - self.b_height) / 2)

    def set_dx0(self):
        self.__dx = 0

    def set_dy0(self):
        self.__dy = 0
